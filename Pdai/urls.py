from django.contrib import admin
from django.urls import path
from Pdai import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("practitioners", views.Practitioners_page, name="Practitioners_page"),
    path("sign-out", views.sign_out, name="sign_out"),
    path("main", views.Patients_page, name="Patients_page"),
    path("shareholders", views.ExcuSummary, name="investors"),
    path("useful-information", views.details, name="details"),
    path("about", views.about, name="about"),
    path("links", views.link, name="links"),
    path("Ex-about", views.Exabout, name="Exabout"),
    # Password reset
    path("submit-pass/",
        auth_views.PasswordResetView.as_view(
            template_name="Pdai/passrest.html",
            html_email_template_name="Pdai/password_reset_email.html",
        ),
        name="submit_pass",
    ),
    path(
        "Password-reset-completed/",
        auth_views.PasswordResetDoneView.as_view(template_name="Pdai/pass_done.html"),
        name="password_reset_done",
    ),
    path(
        "Pass_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="Pdai/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-compelet/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="Pdai/pass_complete.html"
),
        name="password_reset_complete",
    ),
    # path('form', views.form, name='form'),
    path("form/<str:id>", views.rform, name="form"),
    #path('Diabetes_dignosis_model_A', views.SVMPred, name='Diabetes_dignosis_model_A'),
    path("form/diabetes-dignosis-results/<str:id>", views.Rf, name="diabetes-dignosis-results"),
]



