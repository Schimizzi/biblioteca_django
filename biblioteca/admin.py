
from django.contrib import admin
from .models import Libro, Cliente

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    
    #administración para el modelo Libro.
    
    list_display = ('id', 'nombre_libro', 'autor', 'disponible')
    search_fields = ('nombre_libro', 'autor')
    list_filter = ('disponible',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    
    # para el cliente.
    list_display = ('id', 'nombre', 'dni', 'telefono')
    search_fields = ('nombre', 'dni')


