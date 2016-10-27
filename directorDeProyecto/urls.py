from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
    url(r'logout/$',usuario_views.logout_view, name='logout'),
    url(r'crearActividad/$',views.crearActividad,name='crearActividad'),
    url(r'eliminarActividad/$',views.eliminarActividad,name='eliminarActividad'),
    url(r'buscarProyecto/$',views.buscarProyecto,name='buscarProyecto'),
    url(r'(?P<proyecto_id>[0-9]+)/editarProyecto$',views.editarProyectoDP,name='editarProyecto'),
    url(r'proyectosAsignados/$',views.proyectosAsignados,name='proyectosAsignados'),
     
    url(r'(?P<id_actividad>[0-9]+)/editarActividad$',views.editarActividad,name='editarActividad$'),
    url(r'verActividades/$',views.verActividades,name='verActividades'),
     url(r'(?P<id_actividad>[0-9]+)/calificarActividad$',views.calificarActividad,name='calificarActividad'),
    
    
    url(r'$',views.inicio, name='paginaPrincipalDirProyecto'),
]