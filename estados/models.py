from django.db import models


# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)


class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

def __str__(self):
    return "No. ", {self.id}+":", {self.nombre}, self.descripcion