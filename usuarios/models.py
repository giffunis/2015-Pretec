from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    pseudonimo = models.CharField(max_length=15)
    correo = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
