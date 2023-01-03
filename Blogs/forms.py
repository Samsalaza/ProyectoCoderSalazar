from django import forms
from Blogs.models import Blog
from ckeditor.fields import RichTextField
from django.contrib.admin import widgets


class BlogForm(forms.ModelForm):
    titulo = forms.CharField(max_length=50)
    nombre_locacion = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    fecha_publicacion = forms.DateField()
    imagen = forms.ImageField()
    opinion = RichTextField()

    class Meta:
        model = Blog
        fields = ['titulo', 'nombre_locacion', 'autor','fecha_publicacion','imagen','opinion',]