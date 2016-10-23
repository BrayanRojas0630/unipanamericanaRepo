from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




@login_required
def inicio(request):
    return render(request,'directorDeProyecto/PaginaPrincipalDirProyecto.html')

#@login_required
#def crearActividad_view(request):