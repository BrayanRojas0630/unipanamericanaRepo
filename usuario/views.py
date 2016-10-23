from django.shortcuts import render, redirect
from .models import Noticias, Perfil, User

from usuario.forms import login_form
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse


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
