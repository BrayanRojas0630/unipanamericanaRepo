from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
    url(r'logout/$',usuario_views.logout_view, name='logout'),
    url(r'agregarEstudiantes/$',views.agregarEstudiante, name='agregarEstudiante'),
    url(r'crearProyecto/$',views.crearProyecto, name='crearProyecto'),
    url(r'$',views.inicio, name='paginaPrincipalAdmin'),
]