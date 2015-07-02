from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views
from microposts import views
import usuarios
import microposts


urlpatterns = [
    # Examples:
    # url(r'^$', 'pretec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$', usuarios.views.get_registro),
    url(r'^inicio/$', usuarios.views.inicio),
    url(r'^login/$', usuarios.views.login),
    url(r'^logout/$', usuarios.views.logout),
    url('^perfil/(?P<username>[a-zA-Z0-9\\_]+)/$', usuarios.views.pag_perfil),
    url(r'^mi_perfil/$', usuarios.views.mi_perfil),
    url(r'^home/$', usuarios.views.pag_home),
    url(r'^editProfile/$', usuarios.views.editProfile),
    url(r'^set_name/$', usuarios.views.set_name),
    url(r'^set_email/$', usuarios.views.set_email),
    url(r'^set_password/$', usuarios.views.set_password),
    url(r'^microposts/$', microposts.views.set_post),
    url(r'^seguidores/$', usuarios.views.follow),
    url(r'^users/$', usuarios.views.users_view),
    url(r'^busquedaPosts/$', usuarios.views.buscarPosts),
    url(r'^busquedaUsu/$', usuarios.views.buscarUsuario),
    url(r'^mi_perfil/delete/(?P<post_id>\d+)/$', usuarios.views.delete_post, name='deletePost'),

]
