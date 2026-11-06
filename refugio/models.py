from django.db import models

class Especie(models.Model):

    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default='Sin descripción')

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    sexo_choices = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]

    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, default='Sin descripción')
    sexo = models.CharField(max_length=10, choices=sexo_choices)
    edad_aproximada = models.IntegerField()
    imagen = models.URLField(max_length=500)
    especie = models.ForeignKey('Especie', on_delete=models.CASCADE)

    def __str__(self):
        return '[' + str(self.codigo) + ']' + self.nombre
