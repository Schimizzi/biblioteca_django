from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True) 
    telefono = models.CharField(max_length=20) 

    def __str__(self):
        return f"ID Socio: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}, Teléfono: {self.telefono}"

class Libro(models.Model):
    
    autor = models.CharField(max_length=100)
    nombre_libro = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible/Vendido"
        return f"ID Libro: {self.id}, Título: '{self.nombre_libro}', Autor: '{self.autor}' ({estado})"

