from django.contrib import admin

# Register your models here.
from .models import Sede
admin.site.register(Sede)

from .models import Facultad
admin.site.register(Facultad)

from .models import Ciclo
admin.site.register(Ciclo)

from .models import Programa
admin.site.register(Programa)