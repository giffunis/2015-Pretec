from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.shortcuts import render_to_response

# from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail


# creados por nosotros
from usuarios.models import Usuario
from .forms import RegistroForm
from .forms import LoginForm

from .forms import EditNameForm
from .forms import EditEmailForm
from .forms import EditPasswordForm
from .forms import BuscarPost
from .forms import BuscarUsuario
from .forms import SubirFoto

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
            try:
                usuario = Usuario.objects.get(pseudonimo = pseudonimo)
            except Usuario.DoesNotExist:
                messages.error(request, 'El usuario no existe')
            else:
                usuario = Usuario.objects.get(pseudonimo = pseudonimo)
                if usuario.password != password:
                    messages.error(request, 'El nombre de usuario o la contrasena no coinciden')
                else:
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
                    email_titulo = 'Bienvenido a Pretec'
                    email_mensaje = 'Ya eres miembro de este fantastico sitio web donde podras enterarte de todas las novedades tecnologicas segun vayan surgiendo. Bienvenido a la era Tecnologica: dsipretec.herokuapp.com'
                    send_mail(email_titulo, email_mensaje, 'pretcdsi@gmail.com', [correo], fail_silently = False)
                    return render(request, 'registro_completado.html')
    else:
        form = RegistroForm()
    return render(request, 'formulario_registro.html', {'form' : form})



def fotoUsu(request):
    if request.method == 'POST':
        form=SubirFoto(request.POST, request.FILES)
        if form.is_valid():
            #cogemos la foto y la almacenamos en la carpeta correspondiente
            foto = request.FILES['foto']
            ruta = open('/home/alu4635/dsi/practica/2015-Pretec/static/uploads/' + foto.name, 'wb+')
            for chunk in foto.chunks():
                ruta.write(chunk)
            ruta.close()

            #post del usuario para mostrar en su perfil
            usu_post = Post.objects.filter(pseudonimo = request.session['member_id']).order_by('-id')

            #actualizamos el campo foto
            Usuario.objects.filter(pseudonimo=request.session['member_id']).update(foto=foto)

            #todos los datos del usuario para mostrar en el perfil
            query = Usuario.objects.get(pseudonimo=request.session['member_id'])

            context = {
                'user_data': usu_post,
                'foto_usu' : query.foto,
                'pseudonimo': query.pseudonimo,
                'seguidores': seguidores(query.pseudonimo),
                'sigue':sigue(query.pseudonimo),
                'posts':post(query.pseudonimo),
                'logueado': request.session['member_id'],
            }
            print context
            return render_to_response('perfil.html', context, context_instance=RequestContext(request))
    else:
        form=SubirFoto()
    return render(request, 'cambiarFoto.html', {'form' : form})

#Metodo que te lleva a la pagina de confirmacion
def confirmacion(request):
	return render(request, 'confirmacion.html')

#Metodo que sirve para calcular el numero de seguidores
# Seguidores terminado. No tocar.
def seguidores(username):
    aux = Relaciones.objects.filter(sigue = username).count()
    return aux

#Metodo que sirve para calcular el numero de personas a las que sigue
# Sigue terminado. No tocar.
def sigue(username):
    aux = Relaciones.objects.filter(seguidor = username).count()
    return aux

# Follow terminado. No tocar.
def follow(seguidor,sigue):
    relacion = Relaciones.objects.create(
                    seguidor = Usuario.objects.get(pseudonimo = seguidor),
                    sigue = Usuario.objects.get(pseudonimo = sigue),)
    relacion.save()

def unfollow(seguidor, sigue):
    relacion = Relaciones.objects.get(
                    seguidor = Usuario.objects.get(pseudonimo = seguidor),
                    sigue = Usuario.objects.get(pseudonimo = sigue),).delete()
    #relacion.save()

# Post terminado. No tocar.
def post(username):
    aux = Post.objects.filter(pseudonimo = username).count()
    return aux

# Pag_perfil terminado. No tocar.
@comprueba_auth
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
                unfollow(seguidor,seguir)
                messages.success(request, "Ya no sigues a este usuario")
    usuario = Usuario.objects.get(pseudonimo = username)
    foto_visitado = Usuario.objects.get(pseudonimo=username)
    query = Post.objects.filter(pseudonimo=usuario)
    context = {
        'user_data' : query,
        'pseudonimo': usuario.pseudonimo,
        'seguidores': seguidores(username),
        'sigue':sigue(username),
        'posts':post(username),
        'foto_usu': foto_visitado.foto,
        'logueado': request.session['member_id'],
    }
    salida = render_to_response('perfil.html', context, context_instance=RequestContext(request))
    salida.set_cookie('usuario_a_ver', username)
    try:
        relacion = Relaciones.objects.get(sigue = username, seguidor = request.session['member_id'])
    except Relaciones.DoesNotExist:
        salida.set_cookie('lo_sigo', 'no')
    else:
        salida.set_cookie('lo_sigo', 'yes')

    return salida
    #return render(request,'perfil.html', {'pseudonimo': usuario.pseudonimo,'seguidores': seguidores(username), 'sigue':sigue(username), 'posts':post(username)})

# verSigue terminado. No tocar.
@comprueba_auth
def verSigue(request):
    query = Relaciones.objects.filter(seguidor=request.COOKIES.get('usuario_a_ver'))

    context = {
        'sigues': query,
    }

    return render_to_response('siguiendo.html', context, context_instance=RequestContext(request))

# verSeguidores terminado. No tocar.
@comprueba_auth
def verSeguidores(request):
    query = Relaciones.objects.filter(sigue=request.COOKIES.get('usuario_a_ver'))
    context = {
        'seguidores': query,
    }
    return render_to_response('seguidores.html', context, context_instance=RequestContext(request))


@comprueba_auth
def mi_perfil(request):

    usuario = Usuario.objects.get(pseudonimo = request.session['member_id'])
    query = Post.objects.filter(pseudonimo = request.session['member_id']).order_by('-id')

    context = {
        "user_data" : query,
        'foto_usu' : usuario.foto,
        'pseudonimo': usuario.pseudonimo,
        'seguidores': seguidores(usuario.pseudonimo),
        'sigue':sigue(usuario.pseudonimo),
        'posts':post(usuario.pseudonimo),
        'logueado': request.session['member_id'],

    }

    print context
    salida = render_to_response('perfil.html', context, context_instance=RequestContext(request))
    salida.set_cookie('usuario_a_ver', request.session['member_id'])
    return salida


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
            #query = Usuario.objects.filter(pseudonimo__contains=form.cleaned_data['busquedaUsu'])
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
            query = Post.objects.filter(titulo__contains=form.cleaned_data['busqueda'] )

            context = {
                "post_data" : query,
                "busqueda" : busqueda,
            }

            print context
            return render_to_response('postsBuscados.html', context, context_instance=RequestContext(request))

    else:
        form = BuscarPost()
    return render(request, 'busquedaPosts.html', {'form' : form})

def delete_post(request,post_id):
    query = Post.objects.get(id=post_id)
    query.delete()
    return render(request, 'micropost_borrado.html')

@comprueba_auth
def edit_post(request, post_id):
    if request.method == 'POST':
        new_title = request.POST['titulo']
        new_texto = request.POST['texto']
        post = Post.objects.get(pk=post_id)
        post.titulo = new_title
        post.texto = new_texto
        post.save()
        messages.success(request, "Post modificado!")


    query = Post.objects.get(pk=post_id)
    context = {
        'titulo': query.titulo,
        'texto': query.texto,
    }
    return render_to_response('editar_post.html', context, context_instance=RequestContext(request))
    #return render(request, 'editar_post.html', context)
