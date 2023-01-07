from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Blogs.forms import *
from Blogs.models import *

def index (request):
    return render (request, "index.html")


def blogForm (request):
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titulo = info["titulo"]
            nombre_locacion=info["nombre_locacion"]
            autor=info["autor"]
            fecha_publicacion=info["fecha_publicacion"]
            imagen=info["imagen"]
            opinion=info["opinion"]
            

            blog_Form=Blog(titulo=titulo, nombre_locacion=nombre_locacion, autor=autor,fecha_publicacion=fecha_publicacion,imagen=imagen,opinion=opinion)
            blog_Form.save()
            return render (request, "blogSuccessful.html", {"message":"Su reseña se agregó satisfactoriamente"})

    else:
        form=BlogForm

    return render (request, "blogForm.html", {"form": form})


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
            return render (request, "newPlaceSuccessful.html", {"message":"Se ha agregado un nuevo lugar por descubrir"})

    else:
        form=NuevoLugarForm

    return render (request, "newPlaceForm.html", {"form": form})

def newPlaceSearch (request):
    return render(request, "newPlaceSearch.html")

def searchPlace (request):
    if request.GET["nombre_locacion"]:
        nombre_locacion=request.GET["nombre_locacion"]
        places=Nuevo_sitio.objects.filter(nombre_locacion_icontains=nombre_locacion)
        return render(request, "searcResult.html", {"places":places})
    else:
        return render(request, "newPlaceSearch.html", {"message": "Ingrese un nombre de lugar para  buscar"})

def placesList (request):
    places=Nuevo_sitio.objects.all()
    return render(request, "placesList.html", {"places":places})