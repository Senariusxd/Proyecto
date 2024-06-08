from django.contrib import admin
from .models import Enfermedad, Grupos, Historial, Paciente, EF, EM

admin.site.register(Enfermedad)
admin.site.register(Grupos)
admin.site.register(Historial)
admin.site.register(Paciente)
admin.site.register(EF)
admin.site.register(EM)
