from django.contrib import admin

# Register your models here.
from .models import Grupo_De_Investigacion
admin.site.register(Grupo_De_Investigacion)

from .models import Linea_Investigacion
admin.site.register(Linea_Investigacion)

from .models import Fuente_de_Financiacion
admin.site.register(Fuente_de_Financiacion)

from .models import Tipo_Proyecto
admin.site.register(Tipo_Proyecto)

from .models import Maximo_Nivel_Educativo
admin.site.register(Maximo_Nivel_Educativo)

from .models import tipo_Participacion_Proyecto
admin.site.register(tipo_Participacion_Proyecto)

from .models import Nucleo_Basico_Conocimiento
admin.site.register(Nucleo_Basico_Conocimiento)

from .models import Red_de_Coperacion
admin.site.register(Red_de_Coperacion)

from .models import Empresa
admin.site.register(Empresa)

from .models import Sublinea
admin.site.register(Sublinea)

from .models import MacroProyecto
admin.site.register(MacroProyecto)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Producto_de_Investigacion
admin.site.register(Producto_de_Investigacion)

from .models import Jurado
admin.site.register(Jurado)

from .models import Sustentacion
admin.site.register(Sustentacion)