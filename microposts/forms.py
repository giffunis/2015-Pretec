from django import forms
from django.db import models
import datetime
from bootstrap3_datetime.widgets import DateTimePicker

class PostForm(forms.Form):
	titulo = forms.CharField(label='Titulo', max_length=50, min_length=2)
	texto = forms.CharField(label='Texto', max_length=500, min_length=5, widget=forms.Textarea)
	fecha = forms.DateField(initial=datetime.datetime.now().strftime("%m/%d/%Y"))
