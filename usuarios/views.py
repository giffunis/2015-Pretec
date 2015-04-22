
from django.shortcuts import render
from django.http import HttpResponseRedirect
from usuarios.models import Usuario

from .forms import RegistroForm

# Create your views here.
def get_registro(request):
    if request.method == 'POST':
        #crea una instancia de formulario y la llena con los datos del request
        form=RegistroForm(request.POST)
        #if form.equalPassword():
        #form.toBaseDatos()
        #verifica si es valido
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            pseudonimo = form.cleaned_data['pseudonimo']
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password1']
            date  = form.cleaned_data['date']
            usuario = Usuario.objects.create(
                            nombre = nombre,
                            apellidos = apellidos,
                            pseudonimo = pseudonimo,
                            correo = correo,
                            password = password,
                            date = date,)
            usuario.save()
            #return HttpResponseRedirect('#')
            #aqui va el codigo
            return render(request, 'registro_completado.html')

    else:
        form = RegistroForm()

    return render(request, 'formulario_registro.html', {'form' : form})



def formulario_registro(request):
    return render(request, 'formulario_registro.html')
