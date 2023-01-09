from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Blogs.forms import *
from Blogs.models import *
from django.contrib.auth.decorators import login_required
from Accounts.models import userAvatar
from django.contrib.auth.models import User
from Accounts.forms import AvatarForm

def getAvatar(request):
    lista=userAvatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/defaultAvatar.png"
    return imagen

@login_required
def index (request):
    return render (request, "index.html", {"imagen":getAvatar(request)})

@login_required
def blogForm (request):
    autorId=User.objects.get(id=request.user.id)
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo = info["titulo"]
            nombre_locacion=info["nombre_locacion"]
            autor=autorId
            fecha_publicacion=info["fecha_publicacion"]
            imagen=info["imagen"]
            opinion=info["opinion"]
            

            blog_Form=Blog(titulo=titulo, nombre_locacion=nombre_locacion, autor=autor,fecha_publicacion=fecha_publicacion,imagen=imagen,opinion=opinion)
            blog_Form.save()
            return render (request, "blogSuccessful.html", {"message":"Su reseña se agregó satisfactoriamente", "imagen":getAvatar(request)})

    else:
        form=BlogForm

    return render (request, "blogForm.html", {"form": form, "imagen":getAvatar(request)})

@login_required
def newPlaceForm (request):
    if request.method=="POST":
        form=NuevoLugarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_locacion = info["nombre_locacion"]
            direccion=info["direccion"]
            comentario=info["comentario"]
            

            newPlace_Form=Nuevo_sitio(nombre_locacion=nombre_locacion, direccion=direccion,comentario=comentario)
            newPlace_Form.save()
            return render (request, "newPlaceSuccessful.html", {"message":"Se ha agregado un nuevo lugar por descubrir", "imagen":getAvatar(request)})
        else:
            return render(request, "index.html")
    else:
        form=NuevoLugarForm

    return render (request, "newPlaceForm.html", {"form": form, "imagen":getAvatar(request)})

@login_required
def newPlaceSearch (request):
    return render(request, "newPlaceSearch.html", {"imagen":getAvatar(request)})

def searchPlace (request):
    if ("nombre_locacion") in request.GET:
        nombre_locacion=request.GET["nombre_locacion"]
        places=Nuevo_sitio.objects.filter(nombre_locacion=nombre_locacion)
        return render(request, "searchResult.html", {"places":places})
    else:
        return render(request, "newPlaceSearch.html", {"message": "Ingrese un nombre de lugar para  buscar"})

def placesList (request):
    places=Nuevo_sitio.objects.all()
    return render(request, "placesList.html", {"places":places})

def placeDetails (request, id):
    place=Nuevo_sitio.objects.get(id=id)
    return render (request, "placeDetails.html", {"place":place})