from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from datetime import datetime
from bases.views import SinPrivilegios
from .models import *
from .forms import *
from inv.views import Persona
# Create your views here.

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    context_object_name = 'obj'
    success_message="Servicio agregado satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    context_object_name = 'obj'
    success_message="Servicio actualizado satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form) 

class ServicioDetailView(SinPrivilegios, generic.DetailView):
    permission_required = "srv.view_servicio"
    model = Servicio
    template_name = "servicio/servicio_detail.html"
    context_object_name = "obj"

class ServicioView(SinPrivilegios, generic.ListView):
    permission_required = "srv.view_servicio"
    model = Servicio
    template_name = "servicio/servicio_list.html"
    context_object_name = "obj"
    ordering = ['-fc']
    # serializer_class = ServicioSerializer
    # filter_backends = (filters2.DjangoFilterBackend,)
    # filterset_fields = ('fecha', 'factura')
    
    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)
        # context["form"] = ServicioFormFilter(self.request.GET)
        return context
    def get_queryset(self):        
        if self.request.user.is_superuser:            
            return super().get_queryset()        
        p=Persona.objects.filter(user=self.request.user).first()
        if p.rol == Persona.Rol.technic:            
            return super().get_queryset().filter(technic=p)

def nuevoServicio(request):
    template_name="servicio/servicio_form.html"
    reg=Servicio(fecha=datetime.now())
    
    form=ServicioForm()
    context={'form': form,'obj': reg}
    if request.method == 'POST':
        form=ServicioForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('srv:nuevo_servicio')+"?ok") # render(request,"servicio/servicio_detail.html",{'obj':s})
    
    if request.method == 'GET' and 'ok' in request.GET:
    
        print('nuevo***')
        # return render(request,template_name,context)
        # return redirect(reverse('srv:nuevo_servicio'))

    return render(request,template_name,context)

class ServicioNew(VistaBaseCreate):
    model=Servicio
    template_name="servicio/servicio_form.html"
    form_class=ServicioForm
    success_url=reverse_lazy("srv:servicio_list")
    permission_required="srv.add_servicio"
    
    def get(self, request):        
        p=Persona.objects.get(user=self.request.user)
        reg=Servicio(fecha=datetime.now(),technic=p, email=p.user.email)
        form=ServicioForm(instance=reg)            
        context={'form': form,'obj': reg,'p':p}
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        # perfil=PerfilConductor.objects.filter(usuario = self.request.user).first()
        # if perfil and self.request.user.is_superuser == False:
        #     vehiculo = Vehiculo.objects.get(placa=perfil.vehiculo.pk)
        # context ['obj'] = Servicio(fecha = datetime.now())
        return context
    
    def form_invalid(self, form, **kwargs):
        context = super().get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
    
    def form_valid(self, form):
        form.instance.uc = self.request.user        
    #     if perfil:=PerfilConductor.objects.filter(usuario = self.request.user).first():
    #         vehiculo = Vehiculo.objects.get(placa=perfil.vehiculo.pk)
    #         if self.request.user.is_superuser and vehiculo :
    #             form.instance.cedula = 1000000
    #             form.instance.conductor = 'Creado por superuser'                
    #             form.instance.placa = perfil.vehiculo_id
    #         # si es conductor
    #         elif vehiculo :                
    #             form.instance.cedula = vehiculo.conductor.cedula
    #             form.instance.conductor = vehiculo.conductor.nombre
    #             form.instance.placa = vehiculo.placa
            
        return super().form_valid(form)

class ServicioEdit(VistaBaseEdit):
    permission_required="srv.change_Servicio"
    model=Servicio
    template_name="servicio/servicio_form.html"
    form_class=ServicioForm
    success_url=reverse_lazy("srv:servicio_list")
    
    
    def get(self, request, pk):
        try:
            reg = (Servicio.objects.get(id=pk))            
            # perfil = PerfilConductor.objects.filter(usuario = self.request.user).first()
            # # primer validacion id debe pertenecer reg.vehiculo.placa y no es super user
            # if perfil and reg and self.request.user.is_superuser == False:
            #     vehiculo = Vehiculo.objects.get(placa=perfil.vehiculo)
            #     if vehiculo.placa != reg.vehiculo.placa:                                   
            #         messages.success(request,'Id no pertenece al conductor') 
            #         return redirect('elim:gasto_list')
            # Segunda valiacion: estado del registro                
            # if reg and self.request.user.is_superuser == False and reg.estado_aceptacion in[True, False]:                
            #     state_text ='Ninguno'
            #     if reg.estado_aceptacion is None:
            #         state_text= 'Por revisar'                    
            #     elif bool(reg.estado_aceptacion):
            #         state_text = 'Aceptado. No requiere edición'
            #     else: 
            #         state_text = 'Rechazado'
            #     messages.success(request,f'Gasto tiene un estado {state_text}') 
            #     return redirect('elim:gasto_list')

            form = ServicioForm (instance=reg)            
            context = {'form': form,'obj': reg}
            return render(request, self.template_name, context)
        except Servicio.DoesNotExist:
            # return JsonResponse({'error': 'Gasto del conductor no encontrado'}, status=404)
            return render(request, self.template_name, context)
        except Exception as e:
            # Log the error here
            # return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
            return render(request, self.template_name, context)

    def form_invalid(self, form,  **kwargs):
        context = super().get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        form.instance.um = self.request.user       
        # if self.request.user.is_superuser == False and form.instance.estado_aceptacion == True:                
        #     messages.success(self.request,'Se encuentrada aceptado el gasto ') 
        #     return redirect('elim:gasto_list')
        # if perfil:=PerfilConductor.objects.filter(usuario = self.request.user).first():
        #     vehiculo = Vehiculo.objects.get(placa=perfil.vehiculo)
        #     if vehiculo and self.request.user.is_superuser:            
        #         if form.instance.estado_aceptacion is None:                
        #             form.instance.usuario_aceptacion = None
        #             form.instance.usuario_rechazo = None
        #         elif bool(form.instance.estado_aceptacion):                
        #             form.instance.usuario_aceptacion = self.request.user.username                
        #         else:                
        #             form.instance.usuario_rechazo = self.request.user.username        
        #     elif vehiculo and self.request.user.is_superuser == False:                                        
        #         form.instance.cedula = vehiculo.conductor.cedula
        #         form.instance.conductor = vehiculo.conductor.nombre
        return super().form_valid(form)


