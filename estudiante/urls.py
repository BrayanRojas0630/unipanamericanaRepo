from django.conf.urls import url
from usuario import views as usuario_views
from . import views

urlpatterns = [
	url(r'listaProyectos/$',views.listaProyectos,name='listaProyectos'),
    url(r'misActividades/$', views.listaActividades, name='listaActividades'),
    url(r'subirActividad/$', views.subirActividad, name='subirActividad'),
    url(r'logout/$',usuario_views.logout_view, name='logout'),

	url(r'^$',views.inicio, name='paginaPrincipalEstudiante'),
]