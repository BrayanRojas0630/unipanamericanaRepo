from django.conf.urls import url
from administrador import views as admin_views
from directorDeProyecto import views as dirProy_views
from estudiante import views as estudiante_views
from . import views

urlpatterns = [
    url(r'^$',views.index_view, name='index'),
    url(r'(?P<proyecto_id>[0-9]+)/especificarProyecto$',views.especificarProyecto,name='especificarProyecto'),
    url(r'postularseProyecto/$', views.postularseProyecto, name='postularseProyecto'),
    url(r'administrador/$',admin_views.inicio, name='inicioAdmin'),
    url(r'directorProyecto/$',dirProy_views.inicio, name='inicioDP'),
    url(r'estudiante/$',estudiante_views.inicio, name='inicioEstudiante'),
]