from rest_framework import serializers
from .models import Ruta, Conductor

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    # Campo extra para personalizar respuesta (punto extra)
    conductor_nombre = serializers.ReadOnlyField(source='conductor.nombre')
    class Meta:
        model = Ruta
        fields = ['id', 'origen', 'destino', 'horario', 'conductor', 'conductor_nombre']