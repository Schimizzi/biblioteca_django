from django import forms
from .models import Libro, Cliente

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre_libro', 'autor', 'disponible']
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del libro'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre_libro': 'Título del Libro',
            'autor': 'Autor',
            'disponible': 'Disponible en stock'
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'dni', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DNI (sin puntos)'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
        }
        labels = {
            'nombre': 'Nombre del Cliente',
            'dni': 'DNI',
            'telefono': 'Teléfono'
        }
