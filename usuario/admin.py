from django.contrib import admin

# Register your models here.
from .models import Perfil
admin.site.register(Perfil)

from .models import Noticias
admin.site.register(Noticias)
