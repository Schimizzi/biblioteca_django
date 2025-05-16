# Aplicación de Librería en Django

## Funcionalidades Principales

La aplicación ofrece operaciones CRUD (Crear, Leer, Actualizar, Eliminar) completas para libros y clientes, junto con funcionalidades de búsqueda.

### Gestión de Libros
* **Listar Libros:** Muestra todos los libros disponibles en la librería, con detalles como título, autor y estado (disponible/no disponible).
* **Agregar Nuevo Libro:** Permite añadir nuevos libros a la base de datos a través de un formulario.
* **Editar Libro:** Modifica la información de un libro existente.
* **Eliminar Libro:** Remueve un libro de la base de datos.
* **Buscar Libros:** Filtra la lista de libros por título o autor. Esta búsqueda utiliza el objeto `Q` de Django para realizar consultas OR en la base de datos (ej. buscar un término en el título O en el autor).

### Gestión de Clientes
* **Listar Clientes:** Muestra todos los clientes registrados, con su nombre, DNI y teléfono.
* **Agregar Nuevo Cliente:** Permite registrar nuevos clientes mediante un formulario. Se valida que el DNI sea único.
* **Editar Cliente:** Actualiza los datos de un cliente existente.
* **Eliminar Cliente:** Da de baja a un cliente del sistema.
* **Buscar Clientes:** Filtra la lista de clientes por nombre o DNI, utilizando también objetos `Q` para la consulta.


### Panel de Administración
* Django proporciona un panel de administración (`/admin/`) <*admin:admin123*> listo para usar, donde se pueden gestionar los modelos de `Libro` y `Cliente` de forma directa, siempre que se tenga acceso de superusuario.

## Cómo Empezar

1.  **Clonar/Descargar** el proyecto.
2.  **Asegurarse** de tener Django instalado.
3.  **Configurar** la aplicación `biblioteca` en `INSTALLED_APPS` dentro de `libreria_project/settings.py`.
4.  **Crear Migraciones:**
    ```bash
    python manage.py makemigrations biblioteca
    python manage.py migrate
    ```
5.  **(Opcional) Crear un Superusuario** para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```
6.  **Ejecutar el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/` (o la URL que hayas configurado para la app `biblioteca`).
