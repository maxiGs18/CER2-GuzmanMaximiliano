"""
URL configuration for Certamen2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from refugio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicioSesion/', views.inicioSesion, name='inicioSesion'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('', views.home, name='home'),
    path('mascotas/', views.mostrar_mascotas, name='mascotas'),
    path('agregarMascotas/', views.agregarMascotas, name='agregarMascotas'),
    path('agregarEspecie/', views.agregarEspecie, name='agregarEspecie'),
    path('editarMascotas/', views.editarMascota, name='editarMascotas'),\
    path('confirmarEdicionMascota/', views.confirmarCambioMascota, name='confirmarCambioMascota'),
    path('editarEspecie/', views.editarEspecie, name='editarEspecie'),
    path('confirmarEdicionEspecie/', views.confirmarCambioEspecie, name='confirmarCambioEspecie'),
    path('panelGestion/', views.panelGestion, name='panelGestion'),
    path('eliminarMascotas/', views.eliminarMascota, name='eliminarMascotas'),
    path('eliminarEspecie/', views.eliminarEspecie, name='eliminarEspecie'),
]