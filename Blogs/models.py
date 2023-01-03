from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    nombre_locacion = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(auto_now=False, auto_now_add=False)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    opinion = RichTextField(blank=True,null=True)

    def __str__(self) -> str:
         return self.titulo + " " +self.autor

        