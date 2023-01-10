from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Blogs.forms import *
from Blogs.models import *
from django.contrib.auth.decorators import login_required
from Accounts.models import userAvatar
from django.contrib.auth.models import User
from Accounts.forms import AvatarForm
from Blogs.views import BlogForm

def getAvatar(request):
   if request.user.is_authenticated: 
    lista=userAvatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/defaultAvatar.png"
    return imagen

##@login_required
def index (request):
    blogs = Blog.objects.all().order_by('-id')[:4]
    if len(blogs) == 0:
        blog_1 = Blog.objects.none()
        blog_2 = Blog.objects.none()
        blog_3 = Blog.objects.none()
        blog_4 = Blog.objects.none()
    elif len(blogs) == 1:
        blog_1 = blogs[0]
        blog_2 = Blog.objects.none()
        blog_3 = Blog.objects.none()
        blog_4 = Blog.objects.none()
    elif len(blogs) == 2:
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = Blog.objects.none()
        blog_4 = Blog.objects.none()
    elif len(blogs) == 3:
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = blogs[2]
        blog_4 = Blog.objects.none()
    else:     
        blog_1 = blogs[0]
        blog_2 = blogs[1]
        blog_3 = blogs[2]
        blog_4 = blogs[3]
    
    return render(request, "index.html", {"blog_1": blog_1, "blog_2": blog_2, "blog_3": blog_3, "blog_4": blog_4, "imagen": getAvatar(request)}) 
    


#------------------------------------------------------------Seccion de Blog-----------------------------------------------------------------------------------------
@login_required
def blogForm (request):
    autorId=User.objects.get(id=request.user.id) ##request.user.id 
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

def allBlogs (request):
    blogs = Blog.objects.all().order_by('-id') 
    return render(request, "allBlogs.html", {"blogs": blogs, "imagen": getAvatar(request)}) 

def blogPost (request, id):
    readBlog = Blog.objects.get(id = id)
    return render(request, "blogPost.html", {"readBlog" : readBlog, "imagen": getAvatar(request)})

def editBlog (request, id):
    user_name = request.user.get_full_name()
    blog_edit = Blog.objects.get(id = id)
    if user_name == blog_edit.autor or request.user.is_superuser:        
        if request.method == "POST":
            formulario = BlogForm(request.POST, request.FILES)
            if formulario.is_valid():
                datos = formulario.cleaned_data
                info_imagen = datos["imagen"]
                if str(type(info_imagen)) == "<class 'NoneType'>":      # N0 actualiza el objeto de la db si el campoimagen no tiene cambios
                    pass
                elif str(info_imagen) == "False":                       # Si devuelve False  que guarde un None osea nada
                    blog_edit.imagen = None
                else:                                                   # Si entra al else, es por que se le cargo una imagen.
                    blog_edit.imagen = datos["imagen"]

                blog_edit.titulo = datos["titulo"]
                blog_edit.nombre_locacion = datos["nombre_locacion"]
                blog_edit.opinion = datos["opinion"]
                blog_edit.save()

                return render(request, "blogEditSuccessful.html", {"message": "El post ha sido editado exitosamente!", "imagen": getAvatar(request)})
            else:
                formulario_edit = BlogForm(initial={"titulo": blog_edit.titulo, "subtitulo": blog_edit.nombre_locacion, "cuerpo": blog_edit.opinion, "imagen": blog_edit.imagen})
                return render(request, "blogEdit.html", {"form_post" : formulario_edit, "blog_edit": blog_edit, "message": "Intentelo Nuevamente, hubo un error", "imagen": getAvatar(request)})
        else:
            formulario_edit = BlogForm(initial={"titulo": blog_edit.titulo, "nombre_locacion": blog_edit.nombre_locacion, "opinion": blog_edit.opinion, "imagen": blog_edit.imagen})
            return render(request, "blogEdit.html", {"form_post": formulario_edit , "mensaje_publicacion": "Editar un blog", "blog_edit": blog_edit, "imagen": getAvatar(request)})
    else:
        return render(request, "blogEditSuccessful.html", {"message": "No tiene autorizacion de editar esta publicacion!", "imagen": getAvatar(request)})

@ login_required
def deletePost(request, id):
    user_name = request.user.id
    blog_delete = Blog.objects.get(id=id)
    if user_name == blog_delete.autor or request.user.is_superuser:      # Validar que puedas eliminar tus propios posts
        blog_delete.delete()
        return render(request, "blogEditSuccessful.html", {"message": "El post ha sido eliminado exitosamente!"})
    else:
        return render(request, "blogEditSuccessful.html", {"message": "No tiene autorizacion de eliminar esta publicacion!", "avatar": getAvatar(request)})

@ login_required
def userPosts (request):
    user_name = request.user.id
    blogs = Blog.objects.filter(autor = user_name).order_by("-id") # Consulta por id, de mayor a menor (ORDER BY id DESC en SQL)
    return render(request, "userPosts.html", {"blogs": blogs, "imagen": getAvatar(request)}) 

#---------------------------------------------------------------Seccion de lugares----------------------------------------------------------------------------------
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