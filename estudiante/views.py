from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext #enviar variables al template"""
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):
    return render(request,'estudiante/PaginaPrincipalEstudiante.html')