"""biblioteca/urls.py — mapa de rotas do projeto."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acervo.urls')),
]
