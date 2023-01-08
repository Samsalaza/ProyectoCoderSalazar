from django.shortcuts import render
from Accounts.forms import signupForm
from Accounts.models import Users
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def signup (request):


    if request.method=="POST":
        form=signupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render (request, "signupSuccessful.html", {"message":f"El Usuario {username} ha sido registrado correctamente en la base de datos"})
    else:
        form=signupForm()

    return render (request, "signupForm.html", {"form": form})


def profile (request):
    return render(request, "login.html")

def start (request):
    return render(request, "start.html")

#-------login section

def login_request (request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            us=form.cleaned_data.get("username")
            pas=form.cleaned_data.get("password")
            user=authenticate(username=us, password=pas)
            if user is not None:
                login(request, user)
                return render (request, "loginsuccessful.html", {"mensaje": f"Bienvenido {user}"} )
            else:
                return render (request, "login.html",{"mensaje":"usuario o contraseña incorrecto","form":form})
        else: 
            return render (request, "login.html",{"mensaje":"usuario o contraseña incorrecto","form":form})
    
    
    else:
        form=AuthenticationForm()
        return render (request,"login.html", {"form": form})