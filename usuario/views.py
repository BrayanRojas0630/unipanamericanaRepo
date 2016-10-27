from django.shortcuts import render, redirect
from .models import Noticias, Perfil, User
from django.db.models import Q # Def buscar
from administrador.models import Proyecto # Def buscar
from usuario.forms import login_form
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from administrador.models import Proyecto,Red_de_Coperacion,Fuente_de_Financiacion,Maximo_Nivel_Educativo,Nucleo_Basico_Conocimiento,Grupo_De_Investigacion,Linea_Investigacion,tipo_Participacion_Proyecto 



def inicio(request):
    if request.method=='POST':
        query = request.POST.get('q',False)
        print("query")
        if query:    
             qset = (
                    Q(codigo_IES__icontains=query)|
                    Q(nombre_IES__icontains=query) |
                    Q(ano__icontains=query) |
                    Q(semestre__icontains=query)|
                    Q(titulo__icontains=query) |
                    Q(fecha_inicio__icontains=query) |
                    Q(duracion__icontains=query)|
                    Q(objetivo_socioeconomico__icontains=query) |
                    Q(objetivo_proyecto__icontains=query) |
                    Q(resumen_proyecto__icontains=query) |
                    Q(resultados_esperados__icontains=query) |
                    Q(sede__icontains=query)|
                    Q(nombre_materia__icontains=query) |
                    Q(codigo_materia__icontains=query) |
                    Q(grupo_materia__icontains=query) |
                    Q(horas_asignadas_docente__icontains=query) |
                    Q(gasto_total__icontains=query)|
                    Q(tipo_De_gasto__icontains=query) |
                    Q(valor_semana__icontains=query)|
                    Q(perfiles__icontains=query) |
                    Q(estado__icontains=query) |
                    Q(realizo_Sustentacion_publica__icontains=query) |
                    Q(otras_Entidades_Participantes__icontains=query)|
                    Q(asociado_al_area_de_conocimiento__icontains=query) |
                    Q(modalidad_de_seminario__icontains=query)  
                    )
             proyectos = Proyecto.objects.filter(qset)
             context = {'listResults':proyectos,'query':query}
             return render(request,"usuario/Buscar.html",context)
        else:
            return render(request,"usuario/Buscar.html")
    else:
        return render(request,'usuario/Buscar.html')


def index_view(request):
    message=None
    
    noticias=Noticias.objects.all()
    if request.method=='POST':#esta enviando el form de logeo
        form=login_form(request.POST)
        datosPrueba=request.POST['user']+" ºº "+request.POST['password']
        if form.is_valid():
            usernameLlega=request.POST['user']
            passwordLlega=request.POST['password']
            user=authenticate(username=usernameLlega,password=passwordLlega)#dice si los datos que llegan estan en la bd, si si retorna un obejto user si no retornar NOne
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # a este punto mi usuario esta veridico si existe en la bd, solo debo mostrarle susrespectiva interfaz
                    usuario = User.objects.get(username=request.POST['user'])
                    perfil=Perfil.objects.get(fk_authUser=usuario.pk)
                    if perfil.rol=="Administrador":
                        request.session['id']=usuario.pk
                        return redirect('inicioAdmin')
                    else:
                        if perfil.rol=="Director de Proyecto":
                            request.session['id']=usuario.pk
                            return redirect('inicioDP')
                        else:
                            if perfil.rol=="Estudiante":
                                request.session['id']=usuario.pk
                                return redirect('inicioEstudiante')
                else:
                    message="Tu usuario esta inactivo"
                    context = {'listNoticias':noticias,'message':message}
                    return render(request,'usuario/index.html', context)
            else:
                message="Id usuario y/o contraseña incorrecta2"
                context = {'listNoticias':noticias,'message':message,'datosPrueba':datosPrueba}
                return render(request,'usuario/index.html', context)
        else:
             message="Id usuario y/o contraseña incorrecta3"
             context = {'listNoticias':noticias,'message':message}
             return render(request,'usuario/index.html', context)
    else:#debo mostrar mi sistema de noticias
        context = {'listNoticias':noticias}
        return render(request,'usuario/index.html', context)
    
def logout_view(request):
    logout(request)
    return redirect('index')

def especificarProyecto(request, proyecto_id):
    message=None
    
    proyecto=Proyecto.objects.get(pk=proyecto_id)
    grupo_inves=Grupo_De_Investigacion.objects.all()
    linea_invs=Linea_Investigacion.objects.all()
    ti_parti_proy=tipo_Participacion_Proyecto.objects.all()
    nbc=Nucleo_Basico_Conocimiento.objects.all()
    max_nivel_educa=Maximo_Nivel_Educativo.objects.all()
    fuente_financia=Fuente_de_Financiacion.objects.all()
    red_inves=Red_de_Coperacion.objects.all()
    if request.method=="POST":
        message=request.POST['nombreProyecto']+" lo cambio?"
        context={'proyecto':proyecto,'message':message}
        return render(request,"directorDeProyecto/editarProyectoDP.html",context)
      
    else:
        context={'proyecto':proyecto,'lisGrupoInv':grupo_inves,'listLineasInv':linea_invs,
                 'lisTipoParticipacion':ti_parti_proy,'listNbc':nbc, 'listMaxNivelEdu':max_nivel_educa,
                 'listFuenteFinancia':fuente_financia,'listRedInvest':red_inves}
        return render(request,'usuario/especificarProyecto.html',context)

def postularseProyecto(request):
    return render(request,'usuario/PostularseProyecto.html')