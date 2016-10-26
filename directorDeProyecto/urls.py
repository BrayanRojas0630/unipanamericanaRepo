from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
    url(r'logout/$',usuario_views.logout_view, name='logout'),
    url(r'crearActividadCal/$',views.crearActividadCal,name='crearActividadCal'),
    url(r'editarActividad/$',views.editarActividad,name='editarActividad'),
    url(r'eliminarActividad/$',views.eliminarActividad,name='eliminarActividad'),
    url(r'calificarActividad/$',views.calificarActividad,name='calificarActividad'),
    url(r'buscarProyecto/$',views.buscarProyecto,name='buscarProyecto'),
    url(r'$',views.inicio, name='paginaPrincipalDirProyecto'),
]