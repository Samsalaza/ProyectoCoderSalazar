from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField
# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    nombre_locacion = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    imagen = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=None)
    opinion = RichTextUploadingFormField()

    def __str__(self) -> str:
         return self.titulo + " " +self.autor


class Nuevo_sitio (models.Model):
    nombre_locacion = models.CharField( max_length=50)
    direccion= models.CharField( max_length=50)
    comentario = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.nombre_locacion + "-" +self.direccion
    