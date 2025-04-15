from django.urls import path
from django.contrib.auth import views as auth_views

from inv.views import *
from .views import *

urlpatterns = [
    path('dispositivo/',DispositivoView.as_view(), name='dispositivo_list'),    
    path('dispositivo/new',DispositivoNew.as_view(), name='dispositivo_new'),
    path('dispositivo/edit/<int:pk>',DispositivoEdit.as_view(), name='dispositivo_edit'),
    path('dispositivo/delete/<int:pk>',DispositivoDel.as_view(), name='dispositivo_del'),
    
    path('persona/',PersonaView.as_view(), name='persona_list'),    
    path('persona/new',PersonaNew.as_view(), name='persona_new'),
    path('persona/edit/<int:pk>',PersonaEdit.as_view(), name='persona_edit'),
    path('persona/delete/<int:pk>',PersonaDel.as_view(), name='persona_del'),
]