from django import forms
from django.db import models
from usuarios.models import Usuario
from django.utils.translation import gettext as _



# RegistroForm completado. No tocar
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

# LoginForm terminado. No tocar.
class LoginForm(forms.Form):
    pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)

    def clean(self):
        pseudonimo = self.cleaned_data['pseudonimo']
        password = self.cleaned_data['password']
        try:
            usuario = Usuario.objects.get(pseudonimo = pseudonimo)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("El usuario no existe")
        if usuario.password != password:
            raise forms.ValidationError("El nombre de usuario o la contrasena no coinciden")
        return self.cleaned_data


class EditNameForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 50)

# EditEmailForm terminado. No tocar.
class EditEmailForm(forms.Form):
    old_email = forms.EmailField(label='Correo Antiguo')
    new_email = forms.EmailField(label='Correo Nuevo')

# EditPasswordForm terminado. No tocar.
class EditPasswordForm(forms.Form):
    old_password = forms.CharField(label='Contrasena anterior', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva contrasena', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repita la nueva contrasena', widget=forms.PasswordInput)


class BuscarPost(forms.Form):
    busqueda = forms.CharField(label='Titutlo del post', max_length=100, min_length=2)

class BuscarUsuario(forms.Form):
    busquedaUsu = forms.CharField(label='Nombre de usuario', max_length=50, min_length=2)
