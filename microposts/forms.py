from django import forms
from django.db import models
import datetime
from bootstrap3_datetime.widgets import DateTimePicker

class PostForm(forms.Form):
	titulo = forms.CharField(label='Titulo', max_length=30, min_length=2)
	texto = forms.CharField(label='Texto', max_length=200, min_length=5, widget=forms.Textarea)
	fecha = forms.DateField(widget=DateTimePicker(options={"defaultDate":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"format": "DD/MM/YYYY","pickTime": False}))
