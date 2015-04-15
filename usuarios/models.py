# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    pseudonimo = models.CharField(max_length=15)
    correo = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        cadena = 'Nombre: ' + self.nombre + ', Apellidos: ' + self.apellidos + ', Pseudonimo: ' + self.pseudonimo + ', Correo: ' + self.correo + ', Contraseña: ' + self.password
        return cadena

    def get_nombre(self):
        name = 'Nombre: ' + self.nombre
        return name
