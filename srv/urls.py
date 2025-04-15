from django.urls import path

from srv.views import *
from .views import *

urlpatterns = [
    path('servicio/',ServicioView.as_view(), name='servicio_list'),    
    path('servicio/new',ServicioNew.as_view(), name='servicio_new'),
    path('servicio/edit/<int:pk>',ServicioEdit.as_view(), name='servicio_edit'),
    # path('servicio/delete/<int:pk>',ServicioDel.as_view(), name='servicio_del'),
    path('',nuevoServicio, name='nuevo_servicio'),
    path('servicio/gracias/',nuevoServicio, name='gracias'),
]