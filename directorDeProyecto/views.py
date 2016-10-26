from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from administrador.models import Proyecto
from .models import Actividad


@login_required
def inicio(request):
    return render(request,'directorDeProyecto/PaginaPrincipalDirProyecto.html')

@login_required
def crearActividadCal(request):
    message=None
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        try:
            actividad=Actividad()
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.corte=request.POST['corte']
            actividad.nota=request.POST['nota']
            actividad.porcentaje=request.POST['porcentaje']
            actividad.tipo_actividad=request.POST['tipo_actividad']
            actividad.estado=request.POST['estado']
            #actividad.documentoAdjunto=request.POST['documentoAdjunto']
            actividad.observaciones=request.POST['observaciones']
            usuario=User.objects.get(pk=request.session['id'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=usuario
            actividad.idProyecto=proyecto
            actividad.save()
            return redirect('paginaPrincipalDirProyecto')
        except KeyError:
            message="Error no inserto bien los datos" 
            context={'listaProyectos':proyectos,'message':message}
            return render(request,'directorDeProyecto/crearActividadCal.html',context)
    else:
        context={'listaProyectos':proyectos}
        return render(request,'directorDeProyecto/crearActividadCal.html',context)

def crearActividadNoCal(request):
    message=None
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        try:
            actividad=Actividad()
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=None
            actividad.corte=request.POST['corte']
            actividad.nota=""
            actividad.porcentaje=""
            actividad.tipo_actividad=request.POST['tipo_actividad']
            actividad.estado=request.POST['estado']
            #actividad.documentoAdjunto=request.POST['documentoAdjunto']
            actividad.observaciones=request.POST['observaciones']
            usuario=User.objects.get(pk=request.session['id'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=usuario
            actividad.idProyecto=proyecto
            actividad.save()
            return redirect('paginaPrincipalDirProyecto')
        except KeyError:
            message="Error no inserto bien los datos" 
            context={'listaProyectos':proyectos,'message':message}
            return render(request,'directorDeProyecto/crearActividadNoCal.html',context)
    
    else:
        context={'listaProyectos':proyectos}
        return render(request,'directorDeProyecto/crearActividadNoCal.html',context)


def editarActividad(request):
    message=None
    actividades=Actividad.objects.filter(idDirector=request.session['id'])
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        try:
            actividad=Actividad()
            actividad.id=request.POST['idActividad']
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            if request.POST['fechaLimite']!= '':
                actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.corte=request.POST['corte']
            actividad.nota=request.POST['nota']
            actividad.porcentaje=request.POST['porcentaje']
            actividad.tipo_actividad=request.POST['tipo_actividad']
            actividad.estado=request.POST['estado']
           # actividad.documentoAdjunto=request.POST['documentoAdjunto']
            actividad.observaciones=request.POST['observaciones']   
                
            usuario=User.objects.get(pk=request.session['id'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=usuario
            actividad.idProyecto=proyecto
            actividad.save()
            return redirect('paginaPrincipalDirProyecto')
        except KeyError:
            message="Error no inserto bien los datos" 
            context={'listaProyectos':proyectos, 'listaActividaddes':actividades,'message':message}
            return render(request,'directorDeProyecto/editarActividad.html',context)
    else:
        context={'listaProyectos':proyectos, 'listaActividaddes':actividades}
        return render(request,'directorDeProyecto/editarActividad.html',context)


def eliminarActividad(request):
    actividades=Actividad.objects.filter(idDirector=request.session['id'])
    if request.method=="POST":
        actividad=Actividad()
        actividad.id=request.POST['idActividad']
        actividad.delete()
        return redirect('paginaPrincipalDirProyecto')
    else:
       context={'listaActividaddes':actividades}
       return render(request,'directorDeProyecto/eliminarActividad.html',context)
