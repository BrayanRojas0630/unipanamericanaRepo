from django.db import models
from administrador.models import Proyecto
from django.contrib.auth.models import User


class Corte(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    porcentaje=models.IntegerField(blank=True, null=True)
    nota=models.IntegerField(blank=True, null=True)

class Actividad(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    fecha_Limite=models.DateField(blank=True, null=True)
    corte=models.CharField(max_length=100)
    nota=models.CharField(max_length=100)
    porcentaje=models.CharField(max_length=100)
    tipo_actividad=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    documentoAdjunto=models.FileField(upload_to='Documentos/documentsDirector/')
    observaciones=models.CharField(max_length=100)
    idDirector=models.ForeignKey(User,on_delete=models.CASCADE)
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    
class Actividad_Estudiante(models.Model):
    nota=models.IntegerField(blank=True, null=True)
    desarrollo=models.CharField(max_length=100, blank=True, null=True)
    adjunto=models.FileField(upload_to='Documentos/documentsEstudiante/', null=True)
    idActividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    UsuarioEstudiante=models.ForeignKey(User, on_delete=models.CASCADE)
    nombreCorte=models.ForeignKey(Corte, on_delete=models.CASCADE)
