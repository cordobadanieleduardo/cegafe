from django.contrib import admin
from .models import *

class ServicioAdmin(admin.ModelAdmin):
    search_fields = ('fecha','technic'),
    list_display = ['fecha','dispositive','technic','estado','fc','fm','uc','um']
    ordering = ['-id']
    
admin.site.register(Servicio, ServicioAdmin)  