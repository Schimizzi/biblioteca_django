# Aplicación de Librería en Django

Esta aplicación web, desarrollada con el framework Django, permite gestionar una colección de libros y una base de datos de clientes para una Biblioteca.

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

## Estructura y Componentes de Django Utilizados

La aplicación sigue la arquitectura MVT (Modelo-Vista-Plantilla) de Django:

1.  **Modelos (`models.py`):**
    * `Libro`: Define la estructura de los datos de un libro (título, autor, disponibilidad).
    * `Cliente`: Define la estructura de los datos de un cliente (nombre, DNI, teléfono).
    Django ORM (Object-Relational Mapper) se encarga de la interacción con la base de datos.

2.  **Vistas (`views.py`):**
    * Se utilizan **Vistas Basadas en Clases (CBV)** genéricas de Django (`ListView`, `CreateView`, `UpdateView`, `DeleteView`, `TemplateView`) para manejar la lógica de la aplicación.
    * `HomeView`: Muestra la página de inicio.
    * `LibroListView` y `ClienteListView`: Listan los objetos y manejan la lógica de búsqueda. Sobrescriben `get_queryset()` para filtrar resultados y `get_context_data()` para pasar el término de búsqueda a la plantilla.
    * `LibroCreateView`, `ClienteCreateView`: Manejan la creación de nuevos objetos a través de formularios.
    * `LibroUpdateView`, `ClienteUpdateView`: Gestionan la actualización de objetos existentes.
    * `LibroDeleteView`, `ClienteDeleteView`: Controlan la eliminación de objetos.
    * Se utiliza `logging` para registrar información sobre las operaciones de las vistas en la consola del servidor.

3.  **Formularios (`forms.py`):**
    * `LibroForm` y `ClienteForm`: Son `ModelForm` que se generan a partir de los modelos `Libro` y `Cliente` respectivamente. Facilitan la creación y validación de los datos ingresados por el usuario. Incluyen widgets para personalizar la apariencia de los campos en las plantillas.

4.  **Plantillas (`templates/biblioteca/*.html`):**
    * Escritas en HTML con el lenguaje de plantillas de Django.
    * `base.html`: Plantilla base que define la estructura común (navegación, pie de página, carga de Bootstrap CSS/JS).
    * `home.html`: Página de bienvenida.
    * `libro_list.html`, `cliente_list.html`: Muestran las listas de libros y clientes, incluyendo los formularios de búsqueda.
    * `libro_form.html`, `cliente_form.html`: Plantillas para los formularios de creación y edición.
    * `libro_confirm_delete.html`, `cliente_confirm_delete.html`: Páginas de confirmación antes de eliminar un objeto.
    * Utilizan Bootstrap para el diseño y la responsividad.

5.  **URLs (`urls.py`):**
    * `libreria_project/urls.py`: Archivo de URLs principal del proyecto, que incluye las URLs de la aplicación `biblioteca`.
    * `biblioteca/urls.py`: Define las rutas específicas para cada vista de la aplicación `biblioteca` (ej. `/libros/`, `/clientes/nuevo/`, etc.), utilizando `path()` y asociándolas a las vistas correspondientes. Se usa un `app_name` para el namespacing de las URLs.

## Cómo Empezar (Resumen)

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

## Flujo Básico de una Solicitud (Ejemplo: Lista de Libros con Búsqueda)

1.  El usuario navega a `/biblioteca/libros/` o envía el formulario de búsqueda a esa URL (ej. `/biblioteca/libros/?q=Python`).
2.  Django, a través de `urls.py`, dirige la solicitud a `LibroListView`.
3.  El método `get_queryset()` de `LibroListView` se ejecuta:
    * Recoge el parámetro `q` de la solicitud.
    * Si `q` existe, filtra los libros cuyo título o autor contengan el valor de `q`.
    * Devuelve el conjunto de libros (queryset) resultante.
4.  El método `get_context_data()` de `LibroListView` se ejecuta:
    * Añade el `queryset` de libros y el valor de `search_query` (el término de búsqueda) al contexto que se pasará a la plantilla.
5.  Django renderiza la plantilla `biblioteca/libro_list.html` con el contexto proporcionado.
6.  La plantilla muestra el formulario de búsqueda (con el término de búsqueda actual si existe) y la tabla de libros filtrados.

Este README proporciona una visión general de la aplicación. Para detalles más específicos, se recomienda revisar el código de cada archivo mencionado.
