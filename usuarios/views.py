from django.shortcuts import render

# Create your views here.

def formulario_registro(request):
    return render(request, 'formulario_registro.html')
