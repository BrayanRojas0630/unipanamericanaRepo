from django.db import models
from administrador.models import Proyecto
from django.contrib.auth.models import User

class Sede(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    descripcion=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Facultad(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    Descripcion=models.CharField(max_length=100)
    
    idSede=models.ForeignKey(Sede,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
    
class Ciclo(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Programa(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    codigo_programa=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    idFacultad=models.ForeignKey(Facultad,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
