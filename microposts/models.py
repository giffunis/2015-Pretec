from django.db import models
from django import forms
import usuarios
# from usuarios.models import Usuario
# Create your models here.

class Post(models.Model):
	pseudonimo = models.ForeignKey('usuarios.Usuario')
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=240)
	fecha = models.DateField()



	#devuelve el numero de post de un usuario
	def mumero_microposts(pseudon):
		total = Post.objects.get(pseudonimo = pseudon)
		return len(total)
