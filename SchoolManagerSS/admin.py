from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Periodo)
admin.site.register(Seccion)
admin.site.register(Seccion_Abierta)