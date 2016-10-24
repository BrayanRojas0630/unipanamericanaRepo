from django.contrib import admin

# Register your models here.
from .models import Corte
admin.site.register(Corte)

from .models import Actividad
admin.site.register(Actividad)

from .models import Actividad_Estudiante
admin.site.register(Actividad_Estudiante)