from django import forms
from django.db import models

class PostForm(forms.Form):
	titulo = forms.CharField(label='Titulo', max_length=30, min_length=2)
	texto = forms.CharField(label='Texto', max_length=200, min_length=5, widget=forms.Textarea)
	fecha = forms.DateField()
