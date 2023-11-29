
from django import forms
from .models import Autor, Editorial, Resena

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'direccion', 'pais']

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['libro', 'usuario', 'comentario', 'calificacion']
