# biblioteca/models.py
from django.db import models

class Cliente(models.Model):
    # El campo 'socio' (ID) se crea automáticamente por Django como 'id' (AutoField)
    # si no se especifica una clave primaria.
    # Para mantener la similitud con el original, podríamos usar 'socio_id' o renombrar.
    # Por simplicidad, usaremos el 'id' automático de Django y lo referiremos como ID de socio.
    nombre = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True) # Asumimos que el DNI es único
    telefono = models.CharField(max_length=20) # CharField para flexibilidad en formatos de teléfono

    def __str__(self):
        return f"ID Socio: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}, Teléfono: {self.telefono}"

class Libro(models.Model):
    # El campo 'id_libro' se crea automáticamente por Django como 'id' (AutoField).
    autor = models.CharField(max_length=100)
    nombre_libro = models.CharField(max_length=200)
    # El campo 'esta_vendido' podría mapearse a una relación con una Venta,
    # o un simple booleano si solo se quiere marcar.
    # Por ahora, lo mantendremos simple. Si un libro puede ser prestado/devuelto,
    # se necesitaría una lógica más compleja (ej. un campo 'disponible').
    # Para este ejemplo, asumiremos que 'esta_vendido' significa que no está disponible en stock.
    disponible = models.BooleanField(default=True)

    def __str__(self):
        estado = "Disponible" if self.disponible else "No Disponible/Vendido"
        return f"ID Libro: {self.id}, Título: '{self.nombre_libro}', Autor: '{self.autor}' ({estado})"

# La clase Libreria de libreria.py no se traduce directamente a un modelo.
# Sus funcionalidades (agregar/quitar libros/clientes, listarlos)
# serán manejadas por las vistas de Django y el ORM.
# La persistencia de datos (guardar en JSON) es reemplazada por la base de datos de Django.
