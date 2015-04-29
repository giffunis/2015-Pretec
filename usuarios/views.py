
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from usuarios.models import Usuario

from .forms import RegistroForm
from .forms import LoginForm

# Create your views here.


# def decorador(funcion):
#     def funcion_decorada(*args, **kwargs):
#         if()
#         funcion(*args, **kwargs)
#         print "Despues de llamar a la funcion %s" % funcion.__name__
#     return funcion_decorada

def login(request):
    if request.method == 'POST':

        form=LoginForm(request.POST)

        #if form.is_valid():
            # pseudonimo = form.cleaned_data['pseudonimo']
            # password = form.cleaned_data['password']
        try:
            usuario = Usuario.objects.get(pseudonimo = request.POST['pseudonimo'])
            if usuario.password == request.POST['password']:
                request.session['pseudonimo'] = usuario.pseudonimo #cookie
                return render(request, 'perfil.html')
        except Usuario.DoesNotExist:
             return HttpResponse('Tu nombre de usuario o contrasena no coinciden')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})



def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")






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


#Metodo de la clase LoginForm
def pag_inicio(request):
    if request.method == 'POST':

        form=LoginForm(request.POST)

        #if form.is_valid():
            # pseudonimo = form.cleaned_data['pseudonimo']
            # password = form.cleaned_data['password']
        try:
            usuario = Usuario.objects.get(pseudonimo = request.POST['pseudonimo'])
            if usuario.password == request.POST['password']:
                request.session['pseudonimo'] = usuario.pseudonimo
                return render(request, 'perfil.html')
        except Usuario.DoesNotExist:
             return HttpResponse('Tu nombre de usuario o contrasena no coinciden')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})
