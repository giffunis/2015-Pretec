from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pretec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$', views.get_registro),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^perfil/$', views.pag_perfil),
    url(r'^home/$', views.pag_home),
    url(r'^editProfile/$', views.editProfile),
    url(r'^set_name/$', views.set_name),
    #url(r'^set_email/$', views.set_email),
    #url(r'^set_password/$', views.set_password),
]
