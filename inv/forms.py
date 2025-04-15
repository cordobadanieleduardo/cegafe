from django import forms

from .models import *

class DispositivoForm(forms.ModelForm):
    
    attribute = forms.CharField(label="Atributos", required=False, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 10, 'placeholder':'Descripción actual',
        }
    ), min_length=10, max_length=250)
    
    
    observaciones = forms.CharField(label="Observaciones", required=False, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Observaciones',
        }
    ), min_length=10, max_length=100)
    
    
    descripcionActual = forms.CharField(label="Descripción actual", required=False, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 5, 'placeholder':'Descripción actual',
        }
    ), min_length=10, max_length=250)
    
    class Meta:
        model=Dispositivo
        fields=[
            'fecha',
            'descripcion',
            'descripcionActual',
            'estado',
            'placa',
            'placa6',
            'serial',
            'modelo',
            'tipoElemento',
            'unidad',
            'discoDuro',
            'memoria',
            'ram',
            'pantalla',
            'procesador',
            'unidadLectora',
            'marca',
            'sistemaOperativo',
            'guayaSeguridad',
            'mouse',
            'observaciones',
            'salon',
            'ubicacion',
            'type',
            'persona',
            'cuentadanteNumber',
            'status',
            'regional',
            'attribute',
            'types',
            'valor',
            
            ]
        exclude=['numero_registro']
        labels={'descripcion':"Descripción:",
                "estado":"Estado",
                "placa6":"Placa",
                'tipoElemento':'Tipo de elemento:'

                }
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class PersonaForm(forms.ModelForm):
    
    class Meta:
        model=Persona
        fields=['cedula','estado']
        # exclude=['numero_regis']
        labels={"cedula":"Cédula","estado":"Estado"}
        widget={'cedula': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
