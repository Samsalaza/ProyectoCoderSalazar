from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Blogs.forms import BlogForm
from Blogs.models import Blog

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
        formulario=BlogForm

    return render (request, "blogForm.html", {"form": formulario})


def index (request):
    return render (request, "index.html")