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
    url(r'mostrarUsuario/$', views.mostrarUsuarios_view, name='mostrarUsuario'),
    url(r'(?P<usuario_id>[0-9]+)/editarUsuarios$',views.editarUsuario_view,name='editarUsuarios'),
    
    url(r'realizarConvocatoria/$', views.realizarConvocatoria_view, name='realizarConvocatoria'),
    url(r'(?P<proyecto_id>[0-9]+)/cargar_a_convocatoria', views.cargar_a_Convocatoria_view, name='cargar_a_convocatoria'),

    url(r'(?P<usuario_id>[0-9]+)/eliminarUsuarios$',views.eliminarUsuario_view,name='eliminarUsuarios'),
    url(r'$',views.inicio, name='paginaPrincipalAdmin'),

]