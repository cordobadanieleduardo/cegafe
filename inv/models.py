from django.db import models
from bases.models import ClaseModelo
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

import uuid


# Create your models here.

class Persona(ClaseModelo):
    class Rol(models.TextChoices):
        dinamizador="dinamizador",_("Dinamizador")
        technic="tecnico",_("Técnico(a)")
        usuario="usuario",_("Usuario sena")
        contratista="contratista",_("Contratista")
        anonimo="anonimo",_("Anónimo")

    cedula=models.CharField(max_length=20,help_text="Cédula")
    celular=models.CharField(max_length=10,help_text="Número de celular",blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Usuario')
    rol=models.CharField(verbose_name='Rol',max_length=15,choices=Rol,default=Rol.anonimo)
    
    def __str__(self):
        return f'{self.user.get_full_name().capitalize()}'
    
    class Meta:
        verbose_name_plural = 'Personas'


class Dispositivo(ClaseModelo):
    class Regional(models.TextChoices):
        boyaca="15",_("Boyaca")
    
    class Sede(models.TextChoices):
        cegafe="15",_("Cegafe")
        santaclara="16",_("Santa clara")
        ape="17",_("APE")
        itedris="18",_("ITEDRIS")
        gastronomia="19",_("Gastronomia")
        
    class Tipos(models.TextChoices):
        tipo4="4",_("Tipo 4")
        
    class Tipo(models.TextChoices):
        escritorio="escritorio",_("Escritorio")
        portatil="portatil",_("Portatil")
        impresora="impresora",_("Impresora")
        escaner="escaner",_("Escaner")
        tv="tv",_("Televisor")

    class Status(models.TextChoices):
        Creado="creado",_("Creado")        
        Ejecutado="ejecutado",_("Ejecutado")
        mantenimiento="mantenimiento",_("Mantenimiento")
        Facturado="facturado",_("Facturado")
        no_show="no_show",_("NO SHOW")
        
    class Salon(models.TextChoices):
        _default="Default",_("Default")
        _406="406",_("Piso 406")
        _306="306",_("Piso 2 306")     
        _107="107",_("Piso 1")
    
    class Ubicacion(models.TextChoices):
        _default="Default",_("Default")
        _406="406",_("-- 406")
        _306="306",_("-- 306")     
        _107="107",_("-- 107")       
    
    class Legalizado(models.TextChoices):        
        sin_legalizar="sin legalizar",_("Sin legalizar")
        legalizado="legalizado",_("Legalizado")
    
    fecha=models.DateTimeField(null=True,blank=True,verbose_name='Fecha:')
    descripcion=models.CharField(max_length=50,verbose_name='Descripción:')
    descripcionActual=models.CharField(max_length=250,blank=True,null=True,verbose_name='Descripción actual')
    
    
    placa=models.CharField(verbose_name='Placa',max_length=12,blank=True,null=True)     
    placa6=models.CharField(verbose_name='Placa6',max_length=6,blank=True,null=True)
    serial=models.CharField(max_length=10,blank=True,null=True)
    modelo=models.CharField(max_length=50,blank=True,null=True)
    
    tipoElemento=models.CharField(max_length=50,blank=True,null=True,verbose_name='Tipo de elemento')
    unidad=models.CharField(max_length=50,blank=True,null=True)
    discoDuro=models.CharField(max_length=50,blank=True,null=True,verbose_name='Disco duro')
    memoria=models.CharField(max_length=50,blank=True,null=True)
    ram=models.CharField(max_length=50,blank=True,null=True)
    pantalla=models.CharField(max_length=50,blank=True,null=True)
    procesador=models.CharField(max_length=50,blank=True,null=True)
    unidadLectora=models.CharField(max_length=50,blank=True,null=True,verbose_name='Unidad lectora')
    marca=models.CharField(max_length=50,blank=True,null=True)
    sistemaOperativo=models.CharField(max_length=50,blank=True,null=True,verbose_name='Sistema operativo')
    guayaSeguridad=models.CharField(max_length=50,blank=True,null=True,verbose_name='Guaya de seguridad')
    mouse=models.CharField(max_length=100,blank=True,null=True)
    
    observaciones=models.CharField(max_length=100,blank=True,null=True)
    
    
    salon=models.CharField(verbose_name='Salon',max_length=15,choices=Salon,default=Salon._default)
    ubicacion=models.CharField(verbose_name='Ubicacion',max_length=15,choices=Ubicacion,default=Ubicacion._default)
    numero_registo=models.UUIDField(default=uuid.uuid4,max_length=80)
    type=models.CharField(verbose_name='Tipo',max_length=15,choices=Tipo,blank=True,null=True)
    persona=models.ForeignKey(Persona,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Cuentadante')
    cuentadanteNumber=models.CharField(max_length=10,blank=True,null=True,verbose_name='N¬identificación')
    status=models.CharField(verbose_name='Status',max_length=15,choices=Status,default=Status.Creado)
    
    
    regional=models.CharField(verbose_name='Regional',max_length=15,choices=Regional,default=Regional.boyaca)
    sede=models.CharField(verbose_name='Sede',max_length=15,choices=Sede,blank=True,null=True)
    attribute=models.CharField(verbose_name='Atributos',max_length=250,blank=True,null=True)
    
    types=models.CharField(verbose_name='Tipo', choices=Tipos,blank=True,null=True)
    valor=models.DecimalField(verbose_name='Valor',max_digits=14, decimal_places=2, default=0.0)
    
    class Meta:
        verbose_name_plural="Dispositivos"

    def __str__(self):
        return f'{self.descripcion}, Placa: {self.placa}'
    
    def save(self):
        # self.descripcion=self.descripcion.upper()
        return super().save()


