from django.db import models
from django.contrib.auth.models import User


class Grupo_De_Investigacion(models.Model):
    codigo_IES=models.CharField(max_length=50)
    nombre_IES=models.CharField(max_length=100)
    nombre_grupo=models.CharField(max_length=100)
    fecha_inicio_grupo=models.DateField()
    fecha_vigencia_grupo=models.DateField()
    
    def __str__(self):
        return self.codigo_IES
    
    
class Linea_Investigacion(models.Model):
    nombre=models.CharField(max_length=100)
    inscritos=models.CharField(max_length=100)
    finalizados=models.CharField(max_length=100)
    aprobaron=models.CharField(max_length=100)
    cancelaron=models.CharField(max_length=100)
    perdieron=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Fuente_de_Financiacion(models.Model):
    nombre=models.CharField(max_length=100)
    tipoFinanciacion=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    valor=models.FloatField()
    
    def __str__(self):
        return self.nombre
    
    
class Tipo_Proyecto(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Maximo_Nivel_Educativo(models.Model):
    nivel=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nivel
    
    
    
class tipo_Participacion_Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
class Nucleo_Basico_Conocimiento(models.Model):
    area=models.CharField(max_length=100)
    nbc=models.CharField(max_length=100)

    def __str__(self):
        return self.area
    
    
class Red_de_Coperacion(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    fecha_Creacion_Red=models.DateField()
    sector=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Empresa(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    Descripcion=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    
class Sublinea(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    Descripcion=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre    
    
class MacroProyecto(models.Model):
    nombre=models.CharField(max_length=100, primary_key=True)
    descripcion=models.TextField()

    def __str__(self):
        return self.nombre

class Jurado(models.Model):
    nombre=models.CharField(max_length=100)
    areaConocimiento=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    
class Sustentacion(models.Model):
    nombreJurados=models.ForeignKey(Jurado,on_delete=models.CASCADE)
    fecha=models.CharField(max_length=100)
    salon=models.CharField(max_length=100)
    
    
class Proyecto(models.Model):
    codigo_IES=models.CharField(max_length=100, blank=True, null=True)
    nombre_IES=models.CharField(max_length=100)
    ano=models.CharField(max_length=50, blank=True, null=True)
    semestre=models.CharField(max_length=50, blank=True, null=True)
    titulo=models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio=models.DateField(blank=True, null=True)
    duracion=models.CharField(max_length=50, blank=True, null=True)
    objetivo_socioeconomico=models.TextField(blank=True, null=True)
    objetivo_proyecto=models.TextField()
    resumen_proyecto=models.TextField(blank=True, null=True)
    resultados_esperados=models.TextField(blank=True, null=True)
    sede=models.CharField(max_length=50, blank=True, null=True)
    nombre_materia=models.CharField(max_length=50, blank=True, null=True)
    codigo_materia=models.CharField(max_length=50, blank=True, null=True)
    grupo_materia=models.CharField(max_length=50, blank=True, null=True)
    horas_asignadas_docente=models.IntegerField(blank=True, null=True)
    gasto_total=models.FloatField(blank=True, null=True)
    tipo_De_gasto=models.CharField(max_length=100, blank=True, null=True)
    valor_semana=models.FloatField(blank=True, null=True)
    perfiles=models.CharField(max_length=100)
    realizo_Sustentacion_publica=models.CharField(max_length=50, blank=True, null=True)
    otras_Entidades_Participantes=models.CharField(max_length=50, blank=True, null=True)
    asociado_al_area_de_conocimiento=models.CharField(max_length=50, blank=True, null=True)
    finalizado=models.CharField(max_length=50, blank=True, null=True)
    paz_y_salvo=models.CharField(max_length=50, blank=True, null=True)
    modalidad_de_seminario=models.CharField(max_length=50, blank=True, null=True)
    estado=models.CharField(max_length=100)
    cupoMax=models.CharField(max_length=50, blank=True, null=True)
    cupoMin=models.CharField(max_length=50, blank=True, null=True)
    
    
    tipo_proyecto=models.ForeignKey(Tipo_Proyecto, on_delete=models.CASCADE, blank=True, null=True)
    idGrupo_investigacion=models.ForeignKey(Grupo_De_Investigacion, blank=True, null=True, on_delete=models.CASCADE)
    id_lineas_investigacion_asociadas=models.ForeignKey(Linea_Investigacion, blank=True, null=True, on_delete=models.CASCADE)
    tipo_participacion_proyecto=models.ForeignKey(tipo_Participacion_Proyecto, blank=True, null=True, on_delete=models.CASCADE)
    NBC=models.ForeignKey(Nucleo_Basico_Conocimiento, blank=True, null=True, on_delete=models.CASCADE)
    maximo_nivel_educativo=models.ForeignKey(Maximo_Nivel_Educativo, blank=True, null=True, on_delete=models.CASCADE)
    Fuente_de_financiacion=models.ForeignKey(Fuente_de_Financiacion, blank=True, null=True, on_delete=models.CASCADE)
    directorDeProyecto=models.ForeignKey(User, on_delete=models.CASCADE)
    red_investigacion=models.ForeignKey(Red_de_Coperacion, blank=True, null=True, on_delete=models.CASCADE)
    sublinea=models.ForeignKey(Sublinea, blank=True, null=True, on_delete=models.CASCADE)
    empresa=models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.CASCADE)
    nombreMacroProyecto=models.ForeignKey(MacroProyecto, blank=True, null=True, on_delete=models.CASCADE)
    jurado=models.ForeignKey(Jurado, blank=True, null=True, on_delete=models.CASCADE)
    Sustentacion=models.ForeignKey(Sustentacion, blank=True, null=True, on_delete=models.CASCADE)
    
    
    
class Producto_de_Investigacion(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    ano_obtencion_producto=models.CharField(max_length=100)
    mes_obtencion_producto=models.CharField(max_length=100)
    costo_producto=models.FloatField()
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
