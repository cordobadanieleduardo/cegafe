from django import forms
from .models import Servicio
from inv.views import Persona


class ServicioForm(forms.ModelForm):
    
    # name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
    #     attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    # ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=8, max_length=50)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje',
        }
    ), min_length=10, max_length=500)
    
    technic = forms.ModelChoiceField(required=False,
        queryset=Persona.objects.filter(rol=Persona.Rol.technic,estado=True).order_by('user')
    )
    
    class Meta:
        model=Servicio
        fields=['fecha',
                'content',
                'technic',
                'image',
                'dispositive',
                'isComputer',
                'isTv',
                'isEmail',
                'isVideoConferencia',
                'isProblemRed',
                'isScanner',
                'isPrinter',
                'isDb',
                'isKeyboard',
                'isCamera',
                'isWifi',
                'isMicrophone',
                'isMouse',
                'isFileLost',
                'isLaptopMedical',
                'isPantallaAzul',
                'isPowerOff',
                'isAudio',
                'isMantenimiento',
                'qualification',
                'status',
                'email',
            ]
        exclude=['numero_registro']
        labels={'fecha':"Fecha", "technic":"Técnico(a)"}
        # widget={'email': forms.EmailField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['fecha'].widget.attrs['autocomplete'] = "off"
        self.fields['content'].widget.attrs['autofocus'] = "true"
        self.fields['isComputer'].widget.attrs['class'] = "form-check-input"
        self.fields['isProblemRed'].widget.attrs['class'] = "form-check-input"
        self.fields['isScanner'].widget.attrs['class'] = "form-check-input"
        self.fields['isPrinter'].widget.attrs['class'] = "form-check-input"
        self.fields['isMantenimiento'].widget.attrs['class'] = "form-check-input"
        self.fields['isTv'].widget.attrs['class'] = "form-check-input"
        self.fields['isComputer'].widget.attrs['class'] = "form-check-input"
        self.fields['isTv'].widget.attrs['class'] = "form-check-input"
        self.fields['isEmail'].widget.attrs['class'] = "form-check-input"
        self.fields['isVideoConferencia'].widget.attrs['class'] = "form-check-input"
        self.fields['isProblemRed'].widget.attrs['class'] = "form-check-input"
        self.fields['isScanner'].widget.attrs['class'] = "form-check-input"
        self.fields['isPrinter'].widget.attrs['class'] = "form-check-input"
        self.fields['isDb'].widget.attrs['class'] = "form-check-input"
        self.fields['isKeyboard'].widget.attrs['class'] = "form-check-input"
        self.fields['isCamera'].widget.attrs['class'] = "form-check-input"
        self.fields['isWifi'].widget.attrs['class'] = "form-check-input"
        self.fields['isMicrophone'].widget.attrs['class'] = "form-check-input"
        self.fields['isMouse'].widget.attrs['class'] = "form-check-input"
        self.fields['isFileLost'].widget.attrs['class'] = "form-check-input"
        self.fields['isLaptopMedical'].widget.attrs['class'] = "form-check-input"
        self.fields['isPantallaAzul'].widget.attrs['class'] = "form-check-input"
        self.fields['isPowerOff'].widget.attrs['class'] = "form-check-input"
        self.fields['isAudio'].widget.attrs['class'] = "form-check-input"
        self.fields['isMantenimiento'].widget.attrs['class'] = "form-check-input"
        