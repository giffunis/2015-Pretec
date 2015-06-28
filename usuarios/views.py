from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.translation import gettext as _

from django.shortcuts import render_to_response

# from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

# creados por nosotros
from usuarios.models import Usuario
from .forms import RegistroForm
from .forms import LoginForm

from .forms import EditNameForm
from .forms import EditEmailForm
from .forms import EditPasswordForm

from django import forms
from .models import Usuario

from usuarios.models import Relaciones

# Para ver los microposts en el perfil
from django.template import RequestContext
from microposts.models import Post

# Para importar los mensajes del settings.py
from django.contrib import messages


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


# Login terminado. No tocar.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            pseudonimo = form.cleaned_data['pseudonimo']
            password = form.cleaned_data['password']
            request.session['member_id'] = pseudonimo #creacion de la cookie
            return HttpResponseRedirect('/home') #'perfil/',pseudonimo

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


#Metodo que sirve para calcular el numero de seguidores
def seguidores(username):
    aux = Relaciones.objects.filter(sigue = username).count()
    return aux

#Metodo que sirve para calcular el numero de personas a las que sigue
def sigue(username):
    aux = Relaciones.objects.filter(seguidor = username).count()
    return aux

def follow(request, username):
    relacion = Relaciones.objects.create(
                    seguidor = request.session['member_id'],
                    sigue = username,
                    )
    relacion.save()

def post(username):

     aux = Post.objects.filter(pseudonimo = username).count()
     return aux

@comprueba_auth
def pag_perfil(request,username):
    usuario = Usuario.objects.get(pseudonimo = username)
    return render(request,'perfil.html', {'pseudonimo': usuario.pseudonimo,'seguidores': seguidores(username), 'sigue':sigue(username), 'posts':post(username)})


@comprueba_auth
def mi_perfil(request):
    usuario = Usuario.objects.get(pseudonimo = request.session['member_id'])
    query = Post.objects.filter(pseudonimo = request.session['member_id'])

    context = {
        "user_data" : query,
        'pseudonimo': usuario.pseudonimo,
        'seguidores': seguidores(usuario.pseudonimo),
        'sigue':sigue(usuario.pseudonimo),
        'posts':post(usuario.pseudonimo),
    }

    print context
    return render_to_response('perfil.html', context, context_instance=RequestContext(request))



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

# set_email terminado. No tocar.
@comprueba_auth
def set_email(request):
    if request.method == 'POST':
        form = EditEmailForm(request.POST)
        if form.is_valid():
            old_email = form.cleaned_data['old_email']
            new_email = form.cleaned_data['new_email']
            usuario = Usuario.objects.get(pseudonimo = request.session['member_id'])
            if usuario.correo != old_email:
                messages.error(request, 'El correo es erroneo')
            else:
                usuario.correo = new_email
                usuario.save()
                messages.success(request, 'Su correo se ha actualizado')
    else:
        form = EditEmailForm()
    return render(request, 'set_email.html', {'form' : form})



@comprueba_auth
def set_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            #falta comprobar que la contrasena introducida coincida con la que tenia
            usu = Usuario.objects.get(pseudonimo = request.session['member_id'])
            if old_password == usu.password:
                usu.password = new_password1
                usu.save()
                return HttpResponseRedirect('/mi_perfil')
            else:
                return HttpResponse('La contrasena anterior es erronea')
        else:
            form = EditPasswordForm()
        return render(request, 'set_password.html', {'form' : form})
    else:
        form = EditPasswordForm()
    return render(request, 'set_password.html', {'form' : form})

@comprueba_auth
def users_view(request):
    # usuarios = Usuario.objects.values('pseudonimo').order_by('pseudonimo')
    # return render(request, 'users_view.html', {'usuarios' : usuarios})
    usuarios = Usuario.objects.all()
    names_usuarios = []
    for i in range(0,usuarios.count()):
        names_usuarios.append(usuarios[i].pseudonimo)
    return render(request, 'users_view.html', {'usuarios' : names_usuarios})


#funcion que te lleva a la pagina de inicio
def inicio(request):
    return render(request, 'inicio.html')
