# -*- coding: utf-8 -*-

from django.db import models
from django import forms

# Leyenda de las clases
# Campo de caracter obligatorio: *

# Fin de la leyenda




# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 2) # *
    apellidos = models.CharField(max_length = 30) # *
    pseudonimo = models.CharField(primary_key = True, max_length = 30) # *
    correo = models.EmailField(max_length = 30) # *
    password = models.CharField(max_length = 30) # *
    #date = models.DateField() # *

    def __str__(self):
        cadena = 'Nombre: ' + self.nombre + ', Apellidos: ' + self.apellidos + ', Pseudonimo: ' + self.pseudonimo + ', Correo: ' + self.correo + ', Contraseña: ' + self.password
        return cadena

    def get_nombre(self):
        name = 'Nombre: ' + self.nombre
        return name


    def restriccion_edad():
        edad = calc_edad(self)
        if(edad >= 18 ){
            return True
        } else{
            return False
        }
