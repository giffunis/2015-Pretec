from django.db import models
from django import forms
# Create your models here.

class Post(models.Model):
	titulo = forms.CharField(max_length=30)
	texto = forms.CharField(max_length=200)


