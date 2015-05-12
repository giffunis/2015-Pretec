from django.db import models
from django import forms
# Create your models here.

class Post(models.Model	
	pseudonimo = models.CharField(primary_key = True, max_length = 30)
	titulo = models.CharField(max_length=30)
	texto = models.CharField(max_length=200)


