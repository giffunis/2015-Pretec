from django import forms
from django.db import models
from usuarios.models import Usuario



class RegistroForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 50)
    pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
    correo = forms.EmailField(label='Correo')
    password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contrasena', widget=forms.PasswordInput)
    date = forms.DateField()

class LoginForm(forms.Form):
    pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)

class EditNameForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 50)

class EditEmailForm(forms.Form):
    old_email = forms.EmailField(label='Correo Antiguo')
    new_email = forms.EmailField(label='Correo Nuevo')

class EditPasswordForm(forms.Form):
    old_password = forms.CharField(label='Contrasena anterior', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva contrasena', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repita la nueva contrasena', widget=forms.PasswordInput)
