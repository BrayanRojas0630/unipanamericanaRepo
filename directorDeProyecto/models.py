from django.db import models
from administrador.models import Proyecto
from django.contrib.auth.models import User


class Actividad(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    fecha_Limite=models.DateField()
    
    idDirector=models.ForeignKey(User,on_delete=models.CASCADE)
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    
class Actividad_Estudiante(models.Model):
    nota=models.IntegerField(blank=True, null=True)
    desarrollo=models.CharField(max_length=100, blank=True, null=True)
    adjunto=models.CharField(max_length=100, blank=True, null=True)
    
    idActividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    UsuarioEstudiante=models.ForeignKey(User, on_delete=models.CASCADE)
