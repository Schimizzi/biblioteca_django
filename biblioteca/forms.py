from django import forms
from .models import Libro, Cliente

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre_libro', 'autor', 'disponible']
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del libro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del libro'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre_libro': 'Título del Libro',
            'autor': 'Autor',
            'disponible': 'En Stock'
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'dni', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese solo numeros'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de celular sin 0 ni 11'}),
        }
        labels = {
            'nombre': 'Nombre del Cliente',
            'dni': 'DNI',
            'telefono': 'Teléfono'
        }
