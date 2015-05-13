from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def comprueba_auth(funcion):
    def comprueba_login(*args, **kwargs):
        try:
            if(args[0].session['member_id'] != None):
                return funcion(*args, **kwargs)
        except KeyError:
            return HttpResponseRedirect('/login')
    return comprueba_login



@comprueba_auth
def get_post(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            #variable = formulario
            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']
            date  = form.cleaned_data['date']
            #entrada en la base de datos
            post = Post.objects.create(
	                        pseudonimo = request.session['member_id'],
	                        titulo = titulo,
	                        texto = texto,
	                        date = date,)
            post.save()
            return render(request, 'micropost_enviado.html')
    else:
        form = PostForm()
    return render(request, 'formulario_microposts.html', {'form' : form})
