from django.shortcuts import render, render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tipo_Proyecto, Grupo_De_Investigacion, Linea_Investigacion,Fuente_de_Financiacion,Maximo_Nivel_Educativo,tipo_Participacion_Proyecto, Nucleo_Basico_Conocimiento,Red_de_Coperacion, Empresa, MacroProyecto, Sublinea
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
            namemacro =MacroProyecto.objects.filter(nombre=request.POST['nombreMacroProyecto'])
            macroproyecto = MacroProyecto.objects.get(pk=namemacro[0].nombre)
            proyecto.nombreMacroProyecto=macroproyecto
            proyecto.nombre_IES=request.POST['nombreProyecto']
            proyecto.objetivo_proyecto=request.POST['objetivo']

            sublinea1 =Sublinea.objects.filter(nombre=request.POST['sublinea'])
            sublinea2 = Sublinea.objects.get(pk=sublinea1[0].nombre)
            proyecto.sublinea=sublinea2
            
            empresa1 =Empresa.objects.filter(nombre=request.POST['empresa'])
            empresa2 = Empresa.objects.get(pk=empresa1[0].nombre)
            proyecto.empresa=empresa2

                

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
        empresas = Empresa.objects.all()
        macroproyectos = MacroProyecto.objects.all()
        tipo_proyectos= Tipo_Proyecto.objects.all()
        sublineas = Sublinea.objects.all()
        usuariosDirectores=Perfil.objects.filter(rol="Director de Proyecto")
        context={'list_tipoProyectos':tipo_proyectos, 'listDirector':usuariosDirectores, 'listMacroProyecto':macroproyectos, 'listSublinea': sublineas, 'listEmpresa': empresas}
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



@login_required
def registrarUsuario_view(request):
    if request.method == "POST":
        
       
        perfil=Perfil()
      
        try:
            nombreusuario = request.POST['usuario']
            email=request.POST['mail']
            password = request.POST['password']

            user = User.objects.create_user(username=nombreusuario,
                                            email=email,
                                            password=password)

            user.is_staff = True
            user.save()
           
            facultad1 =Facultad.objects.filter(nombre=request.POST['facultad'])
            facultad2 =Facultad.objects.get(pk=facultad1[0].nombre)
            perfil.fkFacultad=facultad2

            nameuser =User.objects.filter(username=request.POST['usuario'])
            usuario1 = User.objects.get(pk=nameuser[0].id)
            perfil.fk_authUser=usuario1 
            perfil.nombre= request.POST['nombre']
            perfil.apellido= request.POST['apellido']
            perfil.documento= request.POST['documento']
            perfil.telefono= request.POST['telefono']
            perfil.celular= request.POST['celular']
            perfil.mail= request.POST['mail']
            perfil.mail_institucional= request.POST['mail_institucional']
            perfil.facultad= request.POST['facultad']
            perfil.nro_Proyectos_a_Cargo= request.POST['nro_proyectos_a_cargo']
            perfil.rol=request.POST['rol']
            perfil.save()
            return render(request,"administrador/PaginaPrincipalAdmin.html")   
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"administrador/PaginaPrincipalAdmin.html")
    else:
        facultad = Facultad.objects.all()
        contexto = {'listFacultad':facultad}
        

        return render(request,'administrador/registrarUsuarios.html',contexto)


@login_required
def listaUsuarios_view(request):
    usuarios= Perfil.objects.all()    
    contexto = {'listUsuarios':usuarios}
    return render(request,'administrador/listaUsuarios.html', contexto)

    

@login_required
def registrarNoticias_view(request):
    usuario=Perfil.objects.filter(fk_authUser=request.session['username'])
    if request.method == "POST":
        noticiaNew=Noticia()
        try:
            noticiaNew.titulo=request.POST['titulo']
            noticiaNew.contenido=request.POST['contenido']
            noticiaNew.fecha_Publicacion=request.POST['fecha_Publicacion']
            userNoticia=Perfil.objects.get(fk_authUser=request.session['fk_authUser'])
            noticiaNew.idPropietario=userNoticia
            noticiaNew.save()
            return render(request,"administrador/PaginaPrincipalAdmin.html") 
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"administrador/PaginaPrincipalAdmin.html")
    else:
        context={'listUsuario':usuario}
        return render(request,'administrador/registrarInformacion.html',context)



@login_required
def mostrarUsuarios_view(request):
    perfiles=Perfil.objects.all()
    contexto = {'listPerfiles':perfiles}
    return render(request,'administrador/mostrarUsuario.html',contexto)

@login_required
def editarUsuario_view(request, usuario_id):
 
    message=None
    
    perfiles=Perfil.objects.get(pk=usuario_id)
    user = User.objects.get(username = perfiles.fk_authUser)



    if request.method=="POST":

        userU = request.POST['usuario']
        firstName= request.POST['nombre']
        lastName = request.POST['apellido']
        emailU = request.POST['mail']

        user.username = userU
        user.first_name = firstName
        user.last_name = lastName
        user.email = emailU

        user.save()

        user1 =User.objects.filter(username=request.POST['usuario'])
        user2 =User.objects.get(username=user1[0].username)
        perfiles.fk_authUser=user2   
        perfiles.nombre= request.POST['nombre']
        perfiles.apellido= request.POST['apellido']
        perfiles.documento= request.POST['documento']
        perfiles.telefono= request.POST['telefono']
        perfiles.celular= request.POST['celular']
        perfiles.mail= request.POST['mail']
        perfiles.mail_institucional= request.POST['mail_institucional']
        perfiles.facultad= request.POST['facultad']
        perfiles.nro_Proyectos_a_Cargo= request.POST['nro_proyectos_a_cargo']
        perfiles.rol=request.POST['rol']
        perfiles.save()
        context={'perfiles':perfiles,'message':message}
        return render(request,"administrador/PaginaPrincipalAdmin.html")  

    else:
        context={'perfiles':perfiles}
        return render(request,'administrador/editarUsuario.html',context)


@login_required
def eliminarUsuario_view(request, usuario_id):
    usuario=Perfil.objects.get(pk=usuario_id)
    user = User.objects.get(username=usuario.fk_authUser)
    usuario.delete()
    user.delete()
    return render(request,"administrador/PaginaPrincipalAdmin.html")
