from django.contrib import admin

# Importação dos modelos
from gestoreventos.models import *

# Register your models here.

admin.site.register(Curso)
admin.site.register(Palestrante)
admin.site.register(Funcionario)
admin.site.register(Evento)
