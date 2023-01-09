from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from mensajeria.views import *

urlpatterns = [
    path("mensajeFormulario", mensajeFormulario , name = "mensajeFormulario"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),

    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
]