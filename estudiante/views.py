from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext #enviar variables al template"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from usuario.models import Perfil
from administrador.models import Proyecto
from directorDeProyecto.models import Actividad, Actividad_Estudiante, Corte


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
        try:
            actividad.desarrollo=request.POST['desarrollo']
            actividad.adjunto=request.POST['desarrolloAdjunto']
            idActividad_copia=Actividad.objects.get(id=request.POST['idActividad'])
            actividad.idActividad=idActividad_copia
            idEstudiante_copia=User.objects.get(pk=request.session["id"])
            actividad.UsuarioEstudiante=idEstudiante_copia
            actividad.save()
            return render(request,"estudiante/PaginaPrincipalEstudiante.html")   
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
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


@login_required
def calificacionesActividad(request):
    actividades_estudiantes=Actividad_Estudiante.objects.filter(UsuarioEstudiante=User.objects.get(pk=request.session['id']))
    context = {'listActividadEstudiante':actividades_estudiantes}
    return render(request, 'estudiante/CalificacionesPorActividad.html', context)

@login_required
def calificacionesCorte(request):
    cortes=Corte.objects.filter(UsuarioEstudiante=User.objects.get(pk=request.session['id']))
    context = {'listCortes':cortes}
    return render(request, 'estudiante/CalificacionesPorCorte.html')