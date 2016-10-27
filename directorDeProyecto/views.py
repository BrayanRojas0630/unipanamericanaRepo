from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from administrador.models import Proyecto,Tipo_Proyecto,Red_de_Coperacion,Fuente_de_Financiacion,Maximo_Nivel_Educativo,Nucleo_Basico_Conocimiento,Grupo_De_Investigacion,Linea_Investigacion,tipo_Participacion_Proyecto 
from .models import Actividad,Actividad_Estudiante,Corte


@login_required
def inicio(request):
    return render(request,'directorDeProyecto/PaginaPrincipalDirProyecto.html')

@login_required
def crearActividad(request):
    message=None
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        try:
            actividad=Actividad()
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.corte=request.POST['corte']
            actividad.porcentaje=request.POST['porcentaje']
            actividad.tipo_actividad=request.POST['tipo_actividad']
            actividad.estado=request.POST['estado']
            actividad.documentoAdjunto=request.FILES['documentoAdjunto']
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
            return render(request,'directorDeProyecto/crearActividad.html',context)
    else:
        context={'listaProyectos':proyectos}
        return render(request,'directorDeProyecto/crearActividad.html',context)

def verActividades(request):
    actividades=Actividad.objects.filter(idDirector=request.session["id"])
    proyect=Actividad.idProyecto
    context={'listaActi':actividades,'listProyect':proyect}
    return render(request,'directorDeProyecto/verActividades.html',context)   

def editarActividad(request,id_actividad):
    message=None
    actividades=Actividad.objects.get(pk=id_actividad)
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        try:
            actividad=Actividad()
            actividad.id=id_actividad
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            if request.POST['fechaLimite']!= '':
                actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.corte=request.POST['corte']
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
            actividades=Actividad.objects.filter(idDirector=request.session["id"])
            proyect=Actividad.idProyecto
            context={'listaActi':actividades,'listProyect':proyect}
            return  render(request,'directorDeProyecto/verActividades.html',context)  
        except KeyError:
            message="Error no inserto bien los datos" 
            context={'listaProyectos':proyectos, 'listaActividaddes':actividades,'message':message}
            return render(request,'directorDeProyecto/editarActividad.html',context)
    else:
        context={'listaProyectos':proyectos, 'actividades':actividades,'message':message}
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




def buscarProyecto(request):
    proyectoUsuario=Proyecto.objects.filter(directorDeProyecto=request.session['id'])
    if request.method=="POST":
        proyectoNombre=Proyecto.objects.get(id=request.POST['buscarProyecto'])
        jurados=proyectoNombre.jurado
        sustentacion=proyectoNombre.Sustentacion
        context={'listaProyecto':proyectoNombre,'listaUsuario':proyectoUsuario, 'listJurado':jurados,
                 'listSustentacion':sustentacion}
        return render(request,"directorDeProyecto/buscarProyectos.html",context)
    else:
        context={'listaUsuario':proyectoUsuario}
        return render(request,"directorDeProyecto/buscarProyectos.html",context)


def proyectosAsignados(request):
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["id"])
    context={'listaProyectos':proyectos}
    return render(request,'directorDeProyecto/proyectosAsignados.html',context)
    
def editarProyectoDP(request, proyecto_id):
    message=None
    
    proyecto=Proyecto.objects.get(pk=proyecto_id)
    tipoProyectoObj=Tipo_Proyecto.objects.all()
    grupo_inves=Grupo_De_Investigacion.objects.all()
    linea_invs=Linea_Investigacion.objects.all()
    ti_parti_proy=tipo_Participacion_Proyecto.objects.all()
    nbc=Nucleo_Basico_Conocimiento.objects.all()
    max_nivel_educa=Maximo_Nivel_Educativo.objects.all()
    fuente_financia=Fuente_de_Financiacion.objects.all()
    dirProyect=User.objects.filter(pk=request.session["id"])
    red_inves=Red_de_Coperacion.objects.all()
    if request.method=="POST":
      #  try:
        proyecto.nombre_IES=request.POST['nombreProyecto']
        #proyecto.nombreMacroProyecto=request.POST['nombreMacroP']
        proyecto.ano=request.POST['ano']
        proyecto.semestre=request.POST['semestre']
        proyecto.titulo=request.POST['titulo']
        proyecto.fecha_inicio=request.POST['fecha_inicio']
        proyecto.duracion=request.POST['duracion']
        proyecto.sede=request.POST['sede']
        proyecto.nombre_materia=request.POST['nombre_materia']
        proyecto.codigo_materia=request.POST['codigo_materia']
        proyecto.grupo_materia=request.POST['grupo_materia']
        proyecto.objetivo_socioeconomico=request.POST['objetivo_socioeconomico']
        proyecto.objetivo_proyecto=request.POST['objetivo_proyecto']
        proyecto.resumen_proyecto=request.POST['resumen_proyecto']
        proyecto.resultados_esperados=request.POST['resultados_esperados']
        
        proyecto.horas_asignadas_docente=request.POST['horas_asignadas_docente']
        #proyecto.gasto_total=request.POST['gasto_total']
        proyecto.tipo_De_gasto=request.POST['tipo_De_gasto']
        #proyecto.valor_semana=request.POST['valor_semana']
        #proyecto.sublinea=request.POST['sublinea']
        #proyecto.empresa=request.POST['empresa']
        proyecto.perfiles=request.POST['perfiles']
        proyecto.realizo_Sustentacion_publica=request.POST['realizo_Sustentacion_publica']
        proyecto.otras_Entidades_Participantes=request.POST['otras_Entidades_Participantes']
        proyecto.asociado_al_area_de_conocimiento=request.POST['asociado_al_area_de_conocimiento']
        proyecto.finalizado=request.POST['finalizado']
        proyecto.paz_y_salvo=request.POST['paz_y_salvo']
        proyecto.modalidad_de_seminario=request.POST['modalidad_de_seminario']
       
        tipoProyectoObj=Tipo_Proyecto.objects.get(nombre=request.POST['tipoProyecto'])
        grupoInvestigacionObj=Grupo_De_Investigacion.objects.get(id=request.POST['grupoInves'])
        lineaInvstObj=Linea_Investigacion.objects.get(id=request.POST['lineaInvesti'])
        tipoParticipacionObj=tipo_Participacion_Proyecto.objects.get(id=request.POST['tipoParticipacionProyecto'])
        nbcObj=Nucleo_Basico_Conocimiento.objects.get(id=request.POST['nucleoBasic'])
        maxNivelEduObj=Maximo_Nivel_Educativo.objects.get(id=request.POST['maximoNivelEducativo'])
        fuenteFinanciaObj=Fuente_de_Financiacion.objects.get(id=request.POST['fuenteFinancia'])
        dirProyectObj=User.objects.get(pk=request.session['id'])
        redInvestigaObje=Red_de_Coperacion.objects.get(id=request.POST['redInvestigacion'])
        
        proyecto.tipo_proyecto=tipoProyectoObj
        proyecto.idGrupo_investigacion=grupoInvestigacionObj
        proyecto.id_lineas_investigacion_asociadas=lineaInvstObj
        proyecto.tipo_participacion_proyecto=tipoParticipacionObj
        proyecto.NBC=nbcObj
        proyecto.maximo_nivel_educativo=maxNivelEduObj
        proyecto.Fuente_de_financiacion=fuenteFinanciaObj
        proyecto.directorDeProyecto=dirProyectObj
        proyecto.red_investigacion=redInvestigaObje
        proyecto.save()
       # message=request.POST['fecha_inicio']
        #context={'proyecto':proyecto,'message':message}
        return redirect('paginaPrincipalDirProyecto')
        #except KeyError:
         #   message="error no inserto bien los datos" 
         #   context={'datosUser':message}
         #   return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
    else:
        context={'proyecto':proyecto,'lisGrupoInv':grupo_inves,'listLineasInv':linea_invs,
                 'lisTipoParticipacion':ti_parti_proy,'listNbc':nbc, 'listMaxNivelEdu':max_nivel_educa,
                 'listFuenteFinancia':fuente_financia,'listDirProyect':dirProyect,'listRedInvest':red_inves,
                 'listTipProy':tipoProyectoObj}
        return render(request,'directorDeProyecto/editarProyectoDP.html',context)
    
def calificarActividad(request,id_actividad):
    actividades=Actividad.objects.get(id=id_actividad)
    activ_estudiante=Actividad_Estudiante.objects.filter(idActividad=id_actividad)
    if request.method=='POST':
        
        acEst=Actividad_Estudiante.objects.get(id=request.POST['idActividad_est'])
        acEst.nota=request.POST['nota']
        acEst.save()
        #prueba=request.POST['idActividad_est']+"  el id del la aterea que acabo de entregar"
        actividades=Actividad.objects.filter(idDirector=request.session["id"])
        proyect=Actividad.idProyecto
        context={'listaActi':actividades,'listProyect':proyect}
        return render(request,'directorDeProyecto/verActividades.html',context) 
    else:
        context={'actividades':actividades,'listActivEst':activ_estudiante}
        return render(request,'directorDeProyecto/calificarActividad.html',context)   
