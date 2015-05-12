from django.db import models
from django import forms
import datetime
# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=200)

	#devuelve el numero de post de un usuario
	def mumero_microposts(pseudon):
		total = Post.objects.get(pseudonimo = pseudon)
		return len(total)


