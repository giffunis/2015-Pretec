from django.db import models
from django import forms

from usuarios.models import Usuario
# Create your models here.

class Post(models.Model):
	pseudonimo = models.ForeignKey(Usuario)
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=240)

	#devuelve el numero de post de un usuario
	def mumero_microposts(pseudon):
		total = Post.objects.get(pseudonimo = pseudon)
		return len(total)


