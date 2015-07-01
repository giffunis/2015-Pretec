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
from .forms import BuscarPost
from .forms import BuscarUsuario

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

# Logout terminado. No tocar.
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request, 'inicio.html')

def authenticate(name, pswd):
    try:
        usuario = Usuario.objects.get(nombre = name)
        if(pswd == usuario.password):
            return usuario
        else:
            return None
    except KeyError:
        return None


# Metodo que sirve para registrarse
# get_registro terminado. No tocar.
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
            # La comprobacion de las contrasenas la lleva a cabo el valido
            try:
                usuario2 = Usuario.objects.get(pseudonimo = pseudonimo)
                messages.error(request, 'El pseudonimo no se encuentra disponible')
            except Usuario.DoesNotExist:
                try:
                    usuario2 = Usuario.objects.get(correo = correo)
                    messages.error(request, 'El correo no se encuentra disponible')
                except Usuario.DoesNotExist:
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

def follow(seguidor,sigue):
    relacion = Relaciones.objects.create(
                    seguidor = Usuario.objects.get(pseudonimo = seguidor),
                    sigue = Usuario.objects.get(pseudonimo = sigue),)
    relacion.save()

def unfollow(request, username):
    relacion = Relaciones.objects.delete(
                    seguidor = request.session['member_id'],
                    sigue = username,)
    relacion.save()

def post(username):
    aux = Post.objects.filter(pseudonimo = username).count()
    return aux

# @comprueba_auth
def pag_perfil(request,username):
    if request.method == 'POST':
        seguir = request.POST['seguir']
        seguidor = request.session['member_id']
        if(seguir == seguidor):
            messages.error(request, "No te puedes seguir a ti mismo, majo!")
        else:
            try:
                relacion = Relaciones.objects.get(sigue = seguir, seguidor = seguidor)

            except Relaciones.DoesNotExist:
                follow(seguidor,seguir)
                messages.success(request, "Siguiendo!!")
            else:
                messages.success(request, "Ya sigues a este usuario!!")

    usuario = Usuario.objects.get(pseudonimo = username)
    query = Post.objects.filter(pseudonimo=usuario)
    context = {
        'user_data' : query,
        'pseudonimo': usuario.pseudonimo,
        'seguidores': seguidores(username),
        'sigue':sigue(username),
        'posts':post(username),
    }
    return render_to_response('perfil.html', context, context_instance=RequestContext(request))
    #return render(request,'perfil.html', {'pseudonimo': usuario.pseudonimo,'seguidores': seguidores(username), 'sigue':sigue(username), 'posts':post(username)})


@comprueba_auth
def mi_perfil(request):
    usuario = Usuario.objects.get(pseudonimo = request.session['member_id'])
    query = Post.objects.filter(pseudonimo = request.session['member_id']).order_by('-id')

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
    query = Post.objects.all().order_by('-id')

    context = {
        "user_data" : query,
    }

    print context
    return render_to_response('home.html', context, context_instance=RequestContext(request))





@comprueba_auth
def editProfile(request):
    if request.is_ajax():
        a = funcionBuscar(request)
        return HttpResponse(a)

    return render(request,'editProfile.html',{'pseudonimo': request.session['member_id']})

# set_name terminado. No tocar.
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
            messages.success(request, 'El nombre y los apellidos se han actualizado correctamente')
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
            elif usuario.correo == new_email:
                messages.error(request, 'El correo es el mismo')
            else:
                try:
                    usuario2 = Usuario.objects.get(correo = new_email)
                    messages.error(request, 'El correo no se encuentra disponible')
                except Usuario.DoesNotExist:
                    usuario.correo = new_email
                    usuario.save()
                    messages.success(request, 'Su correo se ha actualizado')
        # En caso de que el formulario no sea valido
        else:
            form = EditEmailForm()
            return render(request, 'set_email.html', {'form' : form})
    else:
        form = EditEmailForm()
    return render(request, 'set_email.html', {'form' : form})




# set_password terminado. No tocar.
@comprueba_auth
def set_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(request.POST)
        # En el caso de que el formulario sea valido
        if form.is_valid():

            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            # Consulta a la BD
            usuario = Usuario.objects.get(pseudonimo = request.session['member_id'])

            # Aqui se comprueba que las contrasenas coincidan
            if new_password1 != new_password2:
                messages.error(request, 'Las contrasenas no coinciden')
            # y aqui que la vieja sea correcta
            elif usuario.password != old_password:
                messages.error(request, 'La contrasena es incorrecta')
            # Si es correcta se actualiza
            else:
                usuario.password = new_password1
                usuario.save()
                messages.success(request, 'Su contrasena se ha actualizado correctamente')

        # En caso de que el formulario no sea valido
        else:
            form = EditPasswordForm()
        return render(request, 'set_password.html', {'form' : form})
    # si se trata de una peticion get
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

#funcion para buscar usuarios, si el formulrio es correcto te envia a la pagina con los posts que coinciden con la busqueda

@comprueba_auth
def buscarUsuario(request):
    if request.method == 'POST':
        form=BuscarUsuario(request.POST)
        if form.is_valid():
            buscar = form.cleaned_data['busquedaUsu']
            query = Usuario.objects.filter(pseudonimo=buscar)

            context = {
                "usu_data" : query,
                "usuario" : buscar,
            }
            return render_to_response('usuariosBuscados.html', context, context_instance=RequestContext(request))
    else:
        form=BuscarUsuario()
    return render(request, 'busquedaUsuarios.html', {'form' : form})

#funcion para buscar post, si el formulrio es correcto te envia a la pagina con los posts que coinciden con la busqueda

@comprueba_auth
def buscarPosts(request):
    if request.method == 'POST':
        form=BuscarPost(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            query = Post.objects.filter(titulo=busqueda)

            context = {
                "post_data" : query,
                "busqueda" : busqueda,
            }

            print context
            return render_to_response('postsBuscados.html', context, context_instance=RequestContext(request))

    else:
        form = BuscarPost()
    return render(request, 'busquedaPosts.html', {'form' : form})
