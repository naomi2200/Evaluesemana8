"""
URL configuration for transitrack_api project.

The `urlpatterns` list routes URLs to views.
For more information:
https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rutas.views import RutaViewSet, ConductorViewSet


# Router de DRF
router = DefaultRouter()
router.register(r'rutas', RutaViewSet)
router.register(r'conductores', ConductorViewSet)


# URLs principales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]