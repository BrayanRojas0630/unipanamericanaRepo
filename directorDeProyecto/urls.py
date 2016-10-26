from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
    url(r'logout/$',usuario_views.logout_view, name='logout'),
    url(r'crearActividadCal/$',views.crearActividadCal,name='crearActividadCal'),
    url(r'crearActividadNoCal/$',views.crearActividadNoCal,name='crearActividadNoCal'),
    url(r'editarActividad/$',views.editarActividad,name='editarActividad'),
    url(r'eliminarActividad/$',views.eliminarActividad,name='eliminarActividad'),
    url(r'$',views.inicio, name='paginaPrincipalDirProyecto'),
]