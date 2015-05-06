from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# creados por nosotros
from usuarios.models import Usuario
from .forms import RegistroForm
from .forms import LoginForm
from .forms import EditNameForm

# Create your views here.

def comprueba_auth(funcion):
    # @wraps(funcion)
    def comprueba_login(*args, **kwargs):
        try:
            if(args[0].session['member_id'] != None):
                return funcion(*args, **kwargs)
        except KeyError:
            return HttpResponseRedirect('/login')
    return comprueba_login




def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        try:
            usuario = Usuario.objects.get(pseudonimo = request.POST['pseudonimo'])
            if usuario.password == request.POST['password']:
                request.session['member_id'] = usuario.pseudonimo #creacion de la cookie
                # return render(request,'home.html', {'pseudonimo': request.session['member_id']})
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse('Tu nombre de usuario o contrasena no coinciden')
        except Usuario.DoesNotExist:
             return HttpResponse('El nombre de usuario no existe')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def authenticate(name, pswd):
    try:
        usuario = Usuario.objects.get(nombre = name)
        if(pswd == usuario.password):
            return usuario
        else:
            return None
    except KeyError:
        return None


# def decorador(funcion):
#     def funcion_decorada(*args, **kwargs):
#         if()
#         funcion(*args, **kwargs)
#         print "Despues de llamar a la funcion %s" % funcion.__name__
#     return funcion_decorada


# Metodo que sirve para registrarse
def get_registro(request):
    if request.method == 'POST':
        form=RegistroForm(request.POST)
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
            return render(request, 'registro_completado.html')
    else:
        form = RegistroForm()
    return render(request, 'formulario_registro.html', {'form' : form})

# Metodo que sirve para acceder al perfil del usuario
@comprueba_auth
def pag_perfil(request):
    return render(request,'perfil.html', {'pseudonimo': request.session['member_id']})

@comprueba_auth
def pag_home(request):
    return render(request,'home.html', {'pseudonimo': request.session['member_id']})


@comprueba_auth
def editProfile(request):
    return render(request,'editProfile.html',{'pseudonimo': request.session['member_id']})

@comprueba_auth
def set_name(request):
    if request.method == 'POST':
        form = EditNameForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            usu = Usuario.objects.get(pseudonimo = request.session['member_id'])
            usu.nombre = nombre
            usu.apellidos = apellidos
            usu.save()
            return HttpResponseRedirect('/perfil')
        else:
            form = EditNameForm()
        return render(request, 'set_name.html', {'form' : form})
    else:
        form = EditNameForm()
    return render(request, 'set_name.html', {'form' : form})

# def editProfile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data['nombre']
#             apellidos = form.cleaned_data['apellidos']
#             correo = form.cleaned_data['correo']
#             old_password = form.cleaned_data['old_password']
#             new_password1 = form.cleaned_data['new_password1']
#             new_password2 = form.cleaned_data['new_password2']
#             usu = Usuario.objects.get(pseudonimo = request.session['member_id'])
#             usu.nombre = nombre
#             usu.save()
#             return render(request, 'perfil.html')
#     else:
#         form = EditProfileForm()
#     return render(request, 'formulario_edit.html', {'form' : form})
