from django.shortcuts import render
from Accounts.forms import *
from Accounts.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Blogs.views import getAvatar
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
                return render (request, "loginsuccessful.html", {"mensaje": f"Bienvenido {user}", "imagen":getAvatar(request)} )
            else:
                return render (request, "login.html",{"mensaje":"usuario o contraseña incorrecto","form":form})
        else: 
            return render (request, "login.html",{"mensaje":"usuario o contraseña incorrecto","form":form})
    
    
    else:
        form=AuthenticationForm()
        return render (request,"login.html", {"form": form})

@ login_required
def userLogout(request):
    logout(request)
    return render(request, "logoutsuccessful.html", {"message": "Ha cerrado sesion exitosamente!", "imagen": getAvatar(request)})



@login_required
def editProfile(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "signupEditSuccessful.html", {"message":"Perfil editado correctamente"})
        else:
            return render(request, "signupEditForm.html", {"form":form, "nombreusuario":usuario.username, "message":"Error al editar el perfil"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "signupEditForm.html", {"form":form, "nombreusuario":usuario.username})

@login_required
def addAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            oldAvatar=userAvatar.objects.filter(user=request.user)
            if len(oldAvatar)!=0:
                oldAvatar[0].delete()
            newAvatar=userAvatar(user=request.user, imagen=request.FILES["imagen"])
            newAvatar.save()
            return render(request, "avatarSuccessful.html", {"message":"Avatar agregado correctamente","imagen":getAvatar(request) })
        else:
            return render(request, "addAvatar.html", {"form": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request , "addAvatar.html", {"form": form, "usuario": request.user})
