from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from bases.views import SinPrivilegios
from .models import *
from .forms import *

# Create your views here.

class DispositivoView(SinPrivilegios, generic.ListView):
    permission_required="inv.view_dispositivo"
    model=Dispositivo
    template_name="inv/dispositivo_list.html"
    context_object_name="obj"
    ordering = ['-id']
    
class DispositivoNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required="inv.add_dispositivo"
    model=Dispositivo
    template_name="inv/dispositivo_form.html"
    context_object_name = "obj"
    form_class=DispositivoForm
    success_url=reverse_lazy("inv:dispositivo_list")
    success_message="Dispositivo creada satisfactoriamente"

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('**',response  )

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DispositivoEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required="inv.change_dispositivo"
    model=Dispositivo
    template_name="inv/dispositivo_form.html"
    context_object_name = "obj"
    form_class=DispositivoForm
    success_url=reverse_lazy("inv:dispositivo_list")
    success_message="Dispositivo actualizada satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

class DispositivoDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required="inv.delete_dispositivo"
    model=Dispositivo
    template_name='inv/dispositivo_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:dispositivo_list")
    success_message="Dispositivo eliminado satisfactoriamente"


class PersonaView(SinPrivilegios, generic.ListView):
    permission_required="inv.view_persona"
    model=Persona
    template_name="persona/persona_list.html"
    context_object_name="obj"
    
class PersonaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    permission_required="inv.add_persona"
    model=Persona
    template_name="persona/persona_form.html"
    context_object_name = "obj"
    form_class=PersonaForm
    success_url=reverse_lazy("inv:persona_list")
    success_message="Persona creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PersonaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required="inv.change_persona"
    model=Persona
    template_name="persona/persona_form.html"
    context_object_name = "obj"
    form_class=PersonaForm
    success_url=reverse_lazy("inv:persona_list")
    success_message="Persona actualizada satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

class PersonaDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required="inv.delete_persona"
    model=Persona
    template_name='persona/persona_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:persona_list")
    success_message="Persona eliminado satisfactoriamente"
