from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
    url(r'logout/$',usuario_views.logout_view, name='logout'),
    url(r'agregarEstudiantes/$',views.agregarEstudiante, name='agregarEstudiante'),
    url(r'crearProyecto/$',views.crearProyecto, name='crearProyecto'),
    url(r'registrarUsuarios/$',views.registrarUsuario_view, name='registrarUsuarios'),
    url(r'listaUsuarios/$',views.listaUsuarios_view, name='listaUsuarios'),
    url(r'registrarNoticias/$', views.registrarNoticias_view, name='registrarNoticias'),
    url(r'$',views.inicio, name='paginaPrincipalAdmin'),



]