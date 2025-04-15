from django.db import models

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey


class ClaseModelo(models.Model):
    estado=models.BooleanField(default=True)
    fc=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')
    fm=models.DateTimeField(auto_now=True,verbose_name='Fecha Modif.')
    uc=UserForeignKey(auto_user_add=True,related_name='+',verbose_name='U.creación')
    um=UserForeignKey(auto_user=True,related_name='+',verbose_name='U.modif.')

    class Meta:
        abstract=True
