from django.shortcuts import redirect, HttpResponse


def Practitioners_Group(Groups_All = []):
    def auth_Fun(Func):
        def wrapper(request, *args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in Groups_All:
                return(Func(request, *args, **kwargs))
            else:
                return  redirect('home')
        
        return wrapper
    return auth_Fun




            
        
        