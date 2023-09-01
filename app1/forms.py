from django import forms
from .models import *



class FormularioTecnologia(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ('usuario', 'titulo', 'tecnologia', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagenTecnologia')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'tecnologia' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class ActualizacionTecnologia(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ('titulo', 'tecnologia', 'marca', 'modelo', 'descripcion', 'year', 'precio', 'telefonoContacto', 'emailContacto', 'imagenTecnologia')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'tecnologia' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}), 
            }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class Meta:
        fields = ('contrasenia actual', 'nueva_contrasenia1', 'nueva_contrasenia2')