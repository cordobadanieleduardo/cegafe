from django.db import models
from bases.models import ClaseModelo
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from inv.views import Dispositivo,Persona

import uuid
# Create your models here.

class Servicio(ClaseModelo):
    class Medio_pago(models.TextChoices):
        CONTADO = "CONTADO", _("Contado")
        CREDITO = "CREDITO", _("Crédito")
        TRANSFERENCIA = "TRANSFERENCIA", _("Transferencia")

    class Status(models.TextChoices):
        solicitado = "solicitado", _("solicitado")
        Creado = "creado", _("Creado")
        Creado_por = "creado_por", _("Creado por usuario")        
        Ejecutado = "ejecutado", _("Ejecutado")
        proceso = "proceso", _("En proceso")
        terminado = "terminado", _("Terminado")
        noFueNecesario = "noFueNecesario", _("No fue necesario")
        
    
    class Legalizado(models.TextChoices):        
        sin_legalizar = "sin legalizar", _("Sin legalizar")
        Legalizado = "legalizado", _("Legalizado")

    class Sede(models.TextChoices):
        cegafe="15",_("Cegafe")
        santaclara="16",_("Santa clara")
        ape="17",_("APE")
        itedris="18",_("ITEDRIS")
        gastronomia="19",_("Gastronomia")

    fecha=models.DateTimeField(null=True,blank=True)
    numero_registro=models.UUIDField(default=uuid.uuid4,max_length=80,verbose_name="Número de registro")
    content=models.TextField(verbose_name="Problema a reportar",blank=True,null=True,max_length=500)
    technic=models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Técnico(a)",blank=True,null=True)    
    image=models.ImageField(verbose_name="Imagen",upload_to="services",blank=True,null=True)
    
    dispositive=models.ForeignKey(Dispositivo,on_delete=models.CASCADE,max_length=50,verbose_name='Equipo tecnológico',blank=True,null=True)
    
    isComputer=models.BooleanField(verbose_name='Computador',default=False)
    isTv=models.BooleanField(verbose_name='Es TV?',default=False)
    isEmail=models.BooleanField(verbose_name='Es Email?',default=False)
    isVideoConferencia=models.BooleanField(verbose_name='Es video conferencia?',default=False)
    isProblemRed=models.BooleanField(verbose_name='Red',default=False)
    isScanner=models.BooleanField(verbose_name='Escaner',default=False)
    isPrinter=models.BooleanField(verbose_name='Impresora',default=False)
    isDb=models.BooleanField(verbose_name='¿Problema en base de datos?',default=False)
    isKeyboard=models.BooleanField(verbose_name='Teclado',default=False)
    isCamera=models.BooleanField(verbose_name='Cámara',default=False)
    isWifi=models.BooleanField(verbose_name='Wifi',default=False)
    isMicrophone=models.BooleanField(verbose_name='Microfono',default=False)
    isMouse=models.BooleanField(verbose_name='Ratón',default=False)
    isFileLost=models.BooleanField(verbose_name='¿Archivos perdidos?',default=False)
    isLaptopMedical=models.BooleanField(verbose_name='Equipo en mantenimiento',default=False)
    isPantallaAzul=models.BooleanField(verbose_name='Pantalla azul',default=False)
    isPowerOff=models.BooleanField(verbose_name='No enciende?',default=False)
    isAudio=models.BooleanField(verbose_name='Es Audio?',default=False)
    isMantenimiento=models.BooleanField(verbose_name='Solicita mantenimiento',default=False)
    
    
    qualification=models.PositiveSmallIntegerField(verbose_name='Calificacion',default=0, blank=True,null=True)
    status=models.CharField(max_length=15,choices=Status,default=Status.Creado,help_text= "Status",blank=True,null=True)
    email=models.EmailField(max_length=50,blank=True,null=True)
    
    sede=models.CharField(verbose_name='Sede',max_length=15,choices=Sede,blank=True,null=True)
    #TODO
    #es urgente
    #prioridad
    

    def __str__(self):
        return f'{self.fecha}'
    
    def save(self):
        super(Servicio,self).save()

    class Meta:
        verbose_name_plural = 'Servicios'