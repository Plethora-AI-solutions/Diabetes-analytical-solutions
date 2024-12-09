# from django.http import HttpResponse
#from django.http import Http404
from django.shortcuts import redirect, render #get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
# from django.urls import reverse_lazy
from PredictDai import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import token_generator
from django.core.mail import EmailMessage
# from . Doc_Ra import Practitioners_Group
import pickle
import pandas as pd
from .models import predict
from .models import RF_model
import os 
from google.cloud import aiplatform
# from django.contrib.auth.decorators import user_passes_test
# from django.core.exceptions import PermissionDenied

# IndexPage
def home(request):
    return render(request, "Pdai/home.html")


# Register
def register(request):

    if request.method == "POST":
        fname = request.POST["fname"]
        sname = request.POST["sname"]
        email = request.POST["email"].lower()
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=email):
            messages.error(request, "Email already exits! - Enter  or Reset your password")
            
            return render(request, "Pdai/sign-in.html")
            
        if User.objects.filter(password=pass1):
            messages.error(request, "Password already exist!")
            
            return render(request,"Pdai/register.html")
            
        P_user = User.objects.create_user(username=email, email=email, password=pass1)
        P_user.first_name = fname
        P_user.last_name = sname
        P_user.is_active = False
        P_user.save()

        if P_user.username.endswith("@DDSPractitioners.com"):
            Practitioners_Group = Group.objects.get(name="Practitioners")
            P_user.groups.add(Practitioners_Group)
            Prac_subject = "Diabetes diagnosis system"
            Prac_message = render_to_string(
                "practitioner-email.html", {"name": P_user.first_name}
            )
            Prac_BaseEmail = settings.EMAIL_HOST_USER
            Prac_UserEmail = [P_user.username]
            send_mail(Prac_subject, Prac_message, Prac_BaseEmail, Prac_UserEmail)

        elif P_user.username.endswith("@DDSExecutives.com"):
            Executives_Group = Group.objects.get(name="Executives_Summary")
            P_user.groups.add(Executives_Group)
            Executives_SubjectEmail = "Diabetes diagnosis system"
            Executives_MessageEmail = render_to_string(
                "executives-email.html", {"name": P_user.last_name}
            )
            Executives_Base_Email = settings.EMAIL_HOST_USER
            Executives_UserEmail = [P_user.username]
            send_mail(
                Executives_SubjectEmail,
                Executives_MessageEmail,
                Executives_Base_Email,
                Executives_UserEmail,
            )

        else:
            Patients_group = Group.objects.get(name="Patients")
            P_user.groups.add(Patients_group)
            Patients_Subject = "Welcome to our Diabetes system"
            Patients_Message = render_to_string(
                "patients-email.html", {"name": P_user.first_name}
            )
            Patients_BaseEmail = settings.EMAIL_HOST_USER
            Patients_UserEmail = [P_user.username]

            send_mail(
                Patients_Subject,
                Patients_Message,
                Patients_BaseEmail,
                Patients_UserEmail,
            )

        messages.success(
            request, "Please check your EMAIL and click on the link to be Registered!!"
        )

        # Auth email link

        current_site = get_current_site(request)
        email_subject = "Click the link below to be registered!"
        messag2 = render_to_string(
            "email_tem.html",
            {
                "name": P_user.first_name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(P_user.pk)),
                "token": token_generator.make_token(P_user),
            },
        )
        email = EmailMessage(
            email_subject, messag2, settings.EMAIL_HOST_USER, [P_user.email]
        )
        email.fail_silently = True

        email.send()

        return redirect("sign_in")
    return render(request, "Pdai/register.html")


# Activate


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        P_user = User.objects.get(pk=uid)
    except (ValueError, TypeError, P_user.DoesNotExist):
        P_user = None

    if P_user is not None and token_generator.check_token(P_user, token):
        P_user.is_active = True
        P_user.save()
        login(request, P_user)
        return redirect("sign_in")

    else:
        return redirect(request, "failed_message.html")


# SignIn

def sign_in(request):
    if request.method == "POST":
        email1 = request.POST["email1"]
        pass1 = request.POST["pass1"]

        patients = authenticate(username=email1, password=pass1)


        if (
            patients is not None
            and patients.groups.filter(name="Practitioners").exists()
        ):
            login(request, patients)
            return redirect("practitioners_page")

        elif patients is not None and patients.groups.filter(name="Patients").exists():
            login(request, patients)
            return redirect("Patients_page")

        elif (
            patients is not None
            and patients.groups.filter(name="Executives_Summary").exists()
        ):
            login(request, patients)
            return redirect("investors")

        else:
            messages.error(
                request,
                "Please check your credentials, activation email or register an account!",
            )
            return redirect("sign_in") 
        
    return render(request, "Pdai/sign-in.html")


# Sign_out

def sign_out(request):
    logout(request)
    return redirect("home")



# MainPage: Patients and  Practitioners
# @Practitioners_Group(Groups_All=['Practitioners'])
# @user_passes_test(email1, login_url='register')
# @user_passes_test(email2, login_url='check')
@login_required
def Practitioners_page(request):
    
    return render(request, "Pdai/practitioners.html")


@login_required()
def Patients_page(request):
    # pid = None
    # if id is not None:
    #     try:
    #         #slug = RF_model.objects.get(id=id)
    #         pid = User.objects.get(last_name=id)

    #     except:
    #         return Http404()
        
    pid = User.objects.all()
    return render(request, "Pdai/patients-home.html", {'pid':pid})


@login_required()
def ExcuSummary(request):
    return render(request, "Pdai/Excu_Summary.html")


@login_required()
def form(request):
    return render(request, "Pdai/form.html")


@login_required()
def rform(request, id):

    #rf = RF_model.objects.filter(id=id)
    pid = User.objects.all()
    
    return render(request, "Pdai/rf-form.html", {'pid': pid})

#Predict with  SVM model
@login_required()
def SVMPred(request):
    if request.method == "POST":
        SVM = pickle.load(open("SVM.pkl", "rb"))
        db_new = pd.read_csv("db_new.csv")


        HbA1c_level = request.POST["HbA1c_level"]
        blood_glucose_level = request.POST["blood_glucose_level"]
        age = request.POST["age"]
        bmi = request.POST["bmi"]
        hypertension = request.POST["hypertension"]
        fname = request.user.first_name
        sname = request.user.last_name
        email = request.user.username
        
        hypertension1 = (int(hypertension) - db_new["hypertension"].min()) / (
            db_new["hypertension"].max() - db_new["hypertension"].min()
        )

        HbA1c_level1 = (float(HbA1c_level) - db_new["HbA1c_level"].min()) / (
            db_new["HbA1c_level"].max() - db_new["HbA1c_level"].min()
        )

        blood_glucose_level1 = (
            float(blood_glucose_level) - db_new["blood_glucose_level"].min()
        ) / (db_new["blood_glucose_level"].max() - db_new["blood_glucose_level"].min())

        bmi1 = (float(bmi) - db_new[" bmi"].min()) / (
            db_new[" bmi"].max() - db_new[" bmi"].min()
        )

        age1 = (int(age) - db_new["age"].min()) / (
            db_new["age"].max() - db_new["age"].min()
        )

        SvmResults = SVM.predict([[HbA1c_level1, blood_glucose_level1, age1, bmi1, hypertension1]])


        #probaSvmResults = SVM.predict([[hypertension, HbA1c_level, blood_glucose_level, bmi, age]])
        
        if SvmResults[0] == 0:
            SvmResults = "Negative"
        else:
            SvmResults = "Positive"

        result = predict(
            fname=fname,
            sname=sname,
            email=email,
            HbA1c_level=HbA1c_level,
            blood_glucose_level=blood_glucose_level,
            age=age,
            bmi=bmi,
            hypertension=hypertension,
            results=SvmResults,
        )
        result.save()
        
        context = {"Rf_results": SvmResults, "HbA1c_level": HbA1c_level, "blood_glucose_level": blood_glucose_level, "age":age, "bmi": bmi, "hypertension":hypertension }
        

        return render(
            request, "Pdai/rf-results.html", context =context
        )


#Predict with RF model
@login_required()
def Rf(request, id):
    if request.method == "POST":
        
        crrent_direct = os.getcwd()
        Saved_model = os.path.join(crrent_direct, 'Dai_RfM.pkl')
        with open(Saved_model, 'rb') as f:
            RFM = pickle.load(f)
        
        
        # ENDPOINT_ID="8120350767962914816"
        # PROJECT_ID="724667865468"   
        
        
        # endpoint_name=f"projects/{PROJECT_ID}/locations/europe-west8/endpoints/{ENDPOINT_ID}"

        # RFM = aiplatform.Endpoint(endpoint_name=endpoint_name)
        
        db_new = pd.read_csv("db_new.csv")

        HbA1c_level = request.POST["HbA1c_level"]
        blood_glucose_level = request.POST["blood_glucose_level"]
        age = request.POST["age"]
        bmi = request.POST["bmi"]
        hypertension = request.POST["hypertension"]
        fname = request.user.first_name
        snam = request.user.last_name
        email = request.user.email

        hypertension1 = (int(hypertension) - db_new["hypertension"].min()) / (
            db_new["hypertension"].max() - db_new["hypertension"].min()
        )

        HbA1c_level1 = (float(HbA1c_level) - db_new["HbA1c_level"].min()) / (
            db_new["HbA1c_level"].max() - db_new["HbA1c_level"].min()
        )

        blood_glucose_level1 = (
            float(blood_glucose_level) - db_new["blood_glucose_level"].min()
        ) / (db_new["blood_glucose_level"].max() - db_new["blood_glucose_level"].min())

        bmi1 = (float(bmi) - db_new[" bmi"].min()) / (
            db_new[" bmi"].max() - db_new[" bmi"].min()
        )

        age1 = (int(age) - db_new["age"].min()) / (
            db_new["age"].max() - db_new["age"].min()
        )

        Rf_results = RFM.predict([[HbA1c_level1, blood_glucose_level1, age1, bmi1, hypertension1]])

        if Rf_results[0] == 0:
            Rf_results = "Negative"
        else:
            Rf_results = "Positive"

        #proba = RFM.predict_proba([[hypertension, HbA1c_level, blood_glucose_level, bmi, age]])

        # for i in proba:
        # for j, n in enumerate(i):
        # if j == 0 or j == 1:
        # proba = n * 100

        Rresult = RF_model(
        fname=fname,
        sname=snam,
        email=email,
        HbA1c_level=HbA1c_level,
        blood_glucose_level=blood_glucose_level,
        age=age,
        bmi=bmi,
        hypertension=hypertension,
        RF_predicted=Rf_results,
        #RF_prob = proba    
        )

        Rresult.save() 
        
        pid = User.objects.all()
        
        
        context = {
                "Rf_results": Rf_results,
                "HbA1c_level": HbA1c_level,
                "blood_glucose_level": blood_glucose_level,
                "age": age,
                "bmi": bmi,
                "hypertension": hypertension,
                "pid": pid
                
                 
            }
        
        # pid = RF_model.objects.get(id=id)
        # pid = get_object_or_404(RF_model, id=id)


        return render(request, "Pdai/rf-results.html", context=context)

def about(request):
    
    if request.user.is_authenticated:
        
        pid = User.objects.all()
        return render(request, 'Pdai/about.html', {'pid':pid})
    else:
        return redirect('home')

def link(request):
    if request.user.is_authenticated:
        return render(request, 'Pdai/Links.html')
    else:
        return redirect('home')


def Exabout(request):
    return render(request, "Pdai/external-about.html")

def details(request):
    
    if request.user.is_authenticated:
        
        pid = User.objects.all()
        
        return render(request, "Pdai/details.html", {'pid':pid})  
    else:
        return redirect('home')   



