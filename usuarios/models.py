# -*- coding: utf-8 -*-

from django.db import models
from django import forms
import datetime
from microposts.models import Post


# Leyenda de las clases
# Campo de caracter obligatorio: *

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 2) # *
    apellidos = models.CharField(max_length = 30) # *
    pseudonimo = models.CharField(primary_key = True, max_length = 30) # *
    correo = models.EmailField(max_length = 30) # *
    password = models.CharField(max_length = 30) # *
    date = models.DateField() # *
    posts = models.ManyToManyField(Post);
    seguidores = models.ManyToManyField('self', symmetrical = False, through = 'Relaciones');


    def __str__(self):
        cadena = 'Nombre: ' + self.nombre + ', Apellidos: ' + self.apellidos + ', Pseudonimo: ' + self.pseudonimo + ', Correo: ' + self.correo.encode('utf-8') + ', date: ' + str(self.date) + ', Contrasena: ' + self.password
        return cadena

    def get_nombre(self):
        name = 'Nombre: ' + self.nombre
        return name

    def calc_edad(self):
        hoy = datetime.date.today() # 1976-05-26T00:00:00"
        fecha = self.date
        edad = ((hoy - fecha).days) / 365
        return edad

    def restriccion_edad(self):
        edad = Usuario.calc_edad(self)
        if(edad >= 18):
            return True
        return False

#base de datos con los seguidores y a quien esta siguiendo un usuario
class Relaciones(models.Model):
	seguidor =  models.ForeignKey(Usuario, related_name = 'seguidor');
	sigue = models.ForeignKey(Usuario, related_name = 'sigue');


