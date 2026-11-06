from django.contrib import admin
from .models import Mascota

class mascotaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'sexo', 'edad_aproximada', 'imagen', 'especie')
    ordering = ['codigo']

admin.site.register(Mascota, mascotaAdmin)