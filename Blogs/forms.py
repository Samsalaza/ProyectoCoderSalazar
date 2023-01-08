from django import forms
from Blogs.models import Blog, Nuevo_sitio
from ckeditor.fields import RichTextField
from django.contrib.admin import widgets
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogForm(forms.ModelForm):
    titulo = forms.CharField(max_length=50)
    nombre_locacion = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    fecha_publicacion = forms.DateField()
    imagen = forms.ImageField()
    opinion = RichTextUploadingFormField()

    class Meta:
        model = Blog
        fields = ['titulo', 'nombre_locacion', 'autor','fecha_publicacion','imagen','opinion']

class NuevoLugarForm (forms.ModelForm):
    nombre_locacion = forms.CharField( max_length=50)
    direccion = forms.CharField(max_length=50)
    comentario = RichTextField()

    class Meta:
        model = Nuevo_sitio
        fields = ['nombre_locacion','direccion', 'comentario']