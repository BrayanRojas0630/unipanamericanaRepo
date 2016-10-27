from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext #enviar variables al template"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuario.models import Perfil
from administrador.models import Proyecto
from directorDeProyecto.models import Actividad, Actividad_Estudiante


@login_required
def inicio(request):
    return render(request,'estudiante/PaginaPrincipalEstudiante.html')

@login_required
def listaProyectos(request):
    proyectos = Proyecto.objects.all()
    context = {'listProyectos':proyectos}
    return render(request,'estudiante/ConsultarInfoProyecto.html',context)

@login_required
def subirActividad(request):
    user=User.objects.get(pk=request.session["id"])
    if request.method == "POST":
        actividad=Actividad_Estudiante()
       
        actividad.desarrollo=request.POST['desarrollo']
        actividad.adjunto=request.FILES['desarrolloAdjunto']
        idActividad_copia=Actividad.objects.get(id=request.POST['idActividad'])
        actividad.idActividad=idActividad_copia
        idEstudiante_copia=User.objects.get(username=request.session["usuario"])
        actividad.UsuarioEstudiante=idEstudiante_copia
        actividad.save()
        return render(request,"estudiante/PaginaPrincipalEstudiante.html")   
         
    else:
        actividades=Actividad.objects.all()
        context={'listActividades':actividades,'listEstudiante':user}
        return render(request,'estudiante/SubirActividad.html',context)

@login_required
def listaActividades(request):
    actividades = Actividad.objects.all()
    contexto = {'listActividades':actividades}
    return render(request,'estudiante/misActividades.html',contexto)