"""
URL configuration for transitrack_api project.

The `urlpatterns` list routes URLs to views.
For more information:
https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from productos.views import ProductoViewSet, ProveedorViewSet



# Router de DRF
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)


# URLs principales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]