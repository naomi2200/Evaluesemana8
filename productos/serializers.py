from rest_framework import serializers
from .models import Producto, Proveedor

class ProductoSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.ReadOnlyField(source='proveedor.nombre')
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock', 'proveedor', 'proveedor_nombre']
class ProveedorSerializer(serializers.ModelSerializer):
    # Opcional: muestra los productos de este proveedor (relación inversa)
    productos = serializers.StringRelatedField(many=True, read_only=True)
    # Si quieres mostrar solo los nombres de los productos, StringRelatedField funciona.
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'correo', 'productos']   # añadimos 'productos'