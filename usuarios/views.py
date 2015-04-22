
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegistroForm

# Create your views here.
def get_registro(request):
    if request.method == 'POST':
        #crea una instancia de formulario y la llena con los datos del request
        form=RegistroForm(request.POST)
        #verifica si es valido
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistroForm()

    return render(request, 'formulario_registro.html', {'form' : form})

def formulario_registro(request):
    return render(request, 'formulario_registro.html')
