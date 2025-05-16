# biblioteca/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Libro, Cliente
from .forms import LibroForm, ClienteForm
import logging # Import the logging library

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Vista de Inicio
class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'

# Vistas para Libros
class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'
    context_object_name = 'libros'

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Agregar Nuevo Libro'
        context['nombre_boton'] = 'Crear Libro'
        return context

    def form_valid(self, form):
        logger.info("LibroCreateView: Formulario es válido. Guardando libro.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"LibroCreateView: Formulario es inválido. Errores: {form.errors.as_json()}")
        return super().form_invalid(form)


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libro_form.html'
    success_url = reverse_lazy('biblioteca:libro_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Libro'
        context['nombre_boton'] = 'Actualizar Libro'
        return context

    def form_valid(self, form):
        logger.info(f"LibroUpdateView: Formulario para libro PK {self.object.pk} es válido. Actualizando libro.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"LibroUpdateView: Formulario para libro PK {self.kwargs.get('pk')} es inválido. Errores: {form.errors.as_json()}")
        return super().form_invalid(form)

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:libro_list')
    context_object_name = 'libro'

    def post(self, request, *args, **kwargs):
        logger.info(f"LibroDeleteView: Solicitud POST para eliminar libro PK {self.kwargs.get('pk')}")
        return super().post(request, *args, **kwargs)


# Vistas para Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'biblioteca/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'biblioteca/cliente_form.html'
    success_url = reverse_lazy('biblioteca:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Agregar Nuevo Cliente'
        context['nombre_boton'] = 'Crear Cliente'
        return context

    def form_valid(self, form):
        logger.info("ClienteCreateView: Formulario es válido. Guardando cliente.")
        # Aquí podrías agregar un mensaje de éxito si lo deseas, usando Django messages framework
        # from django.contrib import messages
        # messages.success(self.request, '¡Cliente agregado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Loguea los datos del formulario y los errores
        logger.warning(f"ClienteCreateView: Formulario es inválido.")
        logger.warning(f"Datos del formulario: {form.data}")
        logger.warning(f"Errores del formulario: {form.errors.as_json()}") # Muestra los errores como JSON
        # El comportamiento por defecto de CreateView es volver a mostrar el formulario con los errores.
        # Las plantillas que te proporcioné deberían mostrar estos errores.
        return super().form_invalid(form)


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'biblioteca/cliente_form.html'
    success_url = reverse_lazy('biblioteca:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Cliente'
        context['nombre_boton'] = 'Actualizar Cliente'
        return context
    
    def form_valid(self, form):
        logger.info(f"ClienteUpdateView: Formulario para cliente PK {self.object.pk} es válido. Actualizando cliente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"ClienteUpdateView: Formulario para cliente PK {self.kwargs.get('pk')} es inválido. Errores: {form.errors.as_json()}")
        return super().form_invalid(form)

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'biblioteca/cliente_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:cliente_list')
    context_object_name = 'cliente'

    def post(self, request, *args, **kwargs):
        logger.info(f"ClienteDeleteView: Solicitud POST para eliminar cliente PK {self.kwargs.get('pk')}")
        return super().post(request, *args, **kwargs)
