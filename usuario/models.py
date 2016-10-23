from django.contrib.auth.models import User
from administrador.models import Proyecto
from estudiante.models import Ciclo,Programa,Facultad
from django.db import models

class Perfil(models.Model):
    fk_authUser = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    tipo_documento=models.CharField(max_length=100)
    documento=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100, blank= True, null = True)
    celular=models.CharField(max_length=100)
    mail_institucional=models.CharField(max_length=100)
    nro_Proyectos_a_Cargo=models.IntegerField(blank=True, null=True)
    rol=models.CharField(max_length=100)
    
    programa_Consecutivo=models.CharField(max_length=100, blank= True, null = True)
    cod_Programa=models.CharField(max_length=100, blank= True, null = True)
    investigacion=models.CharField(max_length=100, blank= True, null = True)
    nombre_Investigacion_Trabajo_grado=models.CharField(max_length=100, blank= True, null = True)
    nota=models.IntegerField(blank=True, null=True)
    cargo=models.CharField(max_length=100, blank= True, null = True)#este es el rol que estaba en la tabla estudiantes
    rol_Segun_Colciencias=models.CharField(max_length=100, blank= True, null = True)
    nombreMateriaProgramaEstudiante=models.CharField(max_length=100, blank= True, null = True)
    codigoMateriaProgramaEstudiante=models.CharField(max_length=100, blank= True, null = True)
    estadoInscripcion=models.CharField(max_length=100, blank= True, null = True)
    
    fkFacultad=models.ForeignKey(Facultad, on_delete=models.CASCADE, blank=True, null=True)
    fkProyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True, null=True)
    fkCiclo=models.ForeignKey(Ciclo, on_delete=models.CASCADE, blank=True, null=True)
    fkPrograma=models.ForeignKey(Programa, on_delete=models.CASCADE, blank=True, null=True)
    
class Noticias(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    fecha_publicacion=models.CharField(max_length=100)
    propietario=models.ForeignKey(User,on_delete=models.CASCADE)
    enlaceImagen=models.CharField(max_length=500)
    enlaaceVideo=models.CharField(max_length=500)
