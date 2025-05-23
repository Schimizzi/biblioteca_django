
#from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Libro, Cliente
from .forms import LibroForm, ClienteForm
import logging 
from django.db.models import Q

logger = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'

class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'
    context_object_name = 'libros'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('nombre_libro') 
        query = self.request.GET.get('q') 

        if query:
            logger.info(f"LibroListView: Buscando libros con el término: '{query}'")
            queryset = queryset.filter(
                Q(nombre_libro__icontains=query) | Q(autor__icontains=query)
            )
        else:
            logger.info("LibroListView: Mostrando todos los libros (sin término de búsqueda).")
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info("LibroListView: get_context_data ejecutado.")
        context['search_query'] = self.request.GET.get('q', '') 
        context['titulo_pagina'] = 'Lista de Libros'
        if context['search_query']:
             context['titulo_pagina'] += f" (Resultados para '{context['search_query']}')"
        return context


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


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:libro_list')
    context_object_name = 'libro'

    def post(self, request, *args, **kwargs):
        logger.info(f"LibroDeleteView: Solicitud POST para eliminar libro PK {self.kwargs.get('pk')}")
        return super().post(request, *args, **kwargs)



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

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'biblioteca/cliente_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:cliente_list')
    context_object_name = 'cliente'

    def post(self, request, *args, **kwargs):
        logger.info(f"ClienteDeleteView: Solicitud POST para eliminar cliente PK {self.kwargs.get('pk')}")
        return super().post(request, *args, **kwargs)
