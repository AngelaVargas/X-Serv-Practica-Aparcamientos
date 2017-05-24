from django.contrib import admin

# Register your models here

from .models import Aparcamiento
from .models import Usuario
from .models import Comentario
from .models import Seleccionados

admin.site.register(Aparcamiento)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Seleccionados)
