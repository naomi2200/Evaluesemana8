from rest_framework import viewsets, filters
from .models import Ruta, Conductor
from .serializers import RutaSerializer, ConductorSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['origen', 'destino']   # búsqueda por origen o destino

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer