from django.contrib import admin
from .models import *


# Register your models here.

class DispositivoAdmin(admin.ModelAdmin):
    search_fields = ('descripcion'),
    list_display = ['descripcion','type','estado','fc','fm','uc']
    ordering = ['descripcion']
    
class PersonaAdmin(admin.ModelAdmin):
    search_fields = ('cedula','celular'),
    list_display = ['user','rol','cedula','estado','fc','fm','uc']
    ordering = ['cedula']
    
    
admin.site.register(Persona, PersonaAdmin)  
admin.site.register(Dispositivo, DispositivoAdmin)  