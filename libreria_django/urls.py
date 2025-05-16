
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('biblioteca/', include('biblioteca.urls', namespace='biblioteca')),
    path('', include('biblioteca.urls')), 
]
