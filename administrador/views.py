from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tipo_Proyecto, Grupo_De_Investigacion, Linea_Investigacion,Fuente_de_Financiacion,Maximo_Nivel_Educativo,tipo_Participacion_Proyecto, Nucleo_Basico_Conocimiento,Red_de_Coperacion
from django.contrib.auth.models import User
from usuario.models import Perfil 
from estudiante.models import Sede,Facultad,Ciclo,Programa

@login_required
def inicio(request):
    return render(request,'administrador/PaginaPrincipalAdmin.html')


@login_required
def crearProyecto(request):
    if request.method == "POST":
        proyecto=Proyecto()
        try:
            proyecto.nombreMacroProyecto=request.POST['nombreMacroProyecto']
            proyecto.nombre_IES=request.POST['nombreProyecto']
            proyecto.objetivo_proyecto=request.POST['objetivo']
            proyecto.sublinea=request.POST['sublinea']
            proyecto.empresa=request.POST['empresa']
            tipo_proyecto_copia=Tipo_Proyecto.objects.get(nombre=request.POST['producto'])
            proyecto.tipo_proyecto=tipo_proyecto_copia
            proyecto.perfiles=request.POST['perfiles']
            directorDeProyecto_copia=User.objects.get(pk=request.POST['nombreDirector'])
            proyecto.directorDeProyecto=directorDeProyecto_copia
            proyecto.nombreJurados=request.POST['nombreJurados']
            proyecto.save()
            return redirect('paginaPrincipalAdmin')
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"administrador/PaginaPrincipalAdmin.html")
    else:
        tipo_proyectos= Tipo_Proyecto.objects.all()
        usuariosDirectores=Perfil.objects.filter(rol="Director de Proyecto")
        context={'list_tipoProyectos':tipo_proyectos, 'listDirector':usuariosDirectores}
        return render(request,'administrador/CrearProyecto.html',context)


@login_required
def agregarEstudiante(request):
    if request.method == 'POST':
        estudiante=Estudiante()
        usuario=User()
        try:
            # Agregar en la tabla Usuario
            usuario.usuario=request.POST['usuario']
            usuario.nombre= request.POST['nombre']
            usuario.apellido= request.POST['apellido']
            usuario.password= request.POST['password']
            usuario.documento= request.POST['documento']
            usuario.telefono= request.POST['telefono']
            usuario.celular= request.POST['celular']
            usuario.mail= request.POST['mail']
            usuario.mail_institucional= request.POST['mailInstitucional']
            usuario.facultad= request.POST['facultad']
            usuario.rol='Estudiante'
            usuario.save()
            # Agregar en la tabla Estudiante
            estudiante.usuario=request.POST['usuario']
            estudiante.tipo_documento=request.POST['tipoDocumento']
            estudiante.nombres= request.POST['nombre']
            estudiante.apellidos= request.POST['apellido']
            estudiante.password= request.POST['password']
            estudiante.documento= request.POST['documento']
            estudiante.telefono= request.POST['telefono']
            estudiante.otro_Telefono= request.POST['otroTelefono']
            estudiante.celular= request.POST['celular']
            estudiante.mail= request.POST['mail']
            estudiante.mail_institucional= request.POST['mailInstitucional']
            estudiante.investigacion=request.POST['investigacion']
            estudiante.rol='Estudiante'
            sede_copia=Sede.objects.get(nombre=request.POST['sede'])
            estudiante.sede=sede_copia
            facultad_copia=Facultad.objects.get(nombre=request.POST['facultad'])
            estudiante.facultad=facultad_copia
            ciclo_copia=Ciclo.objects.get(nombre=request.POST['ciclo'])
            estudiante.ciclo=ciclo_copia
            programa_copia=Programa.objects.get(nombre=request.POST['programa'])
            estudiante.programa=programa_copia
            proyecto_copia=Proyecto.objects.get(id=request.POST['idProyecto'])
            estudiante.proyecto=proyecto_copia
            estudiante.save()
            return render(request,"administrador/AgregarEstudiante.html")
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,'administrador/AgregarEstudiante.html',context)
    else:
        proyectos= Proyecto.objects.all()
        sedes= Sede.objects.all()
        facultad=Facultad.objects.all()
        ciclos=Ciclo.objects.all()
        programas=Programa.objects.all()
        contexto = {'listProyectos':proyectos, 'listSedes':sedes, 'listFacultad':facultad, 'listCiclos':ciclos, 'listProgramas':programas}
        return render(request,'administrador/AgregarEstudiante.html',contexto)
    return None
