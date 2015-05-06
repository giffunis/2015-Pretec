from django import forms
from django.db import models
from usuarios.models import Usuario
from django.utils.translation import gettext as _




class RegistroForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 50)
    pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
    correo = forms.EmailField(label='Correo')
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contrasena', widget=forms.PasswordInput)
    date = forms.DateField()

    def clean(self):
    	if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
        	if self.cleaned_data['password1'] != self.cleaned_data['password2']:
        		raise forms.ValidationError(_(u'las contrasenas no coinciden'))
        return self.cleaned_data
		

class LoginForm(forms.Form):
    pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)


class EditProfileForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 50)
    correo = forms.EmailField(label='Correo')
    old_password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repita la contrasena', widget=forms.PasswordInput)
