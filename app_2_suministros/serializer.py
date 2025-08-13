from rest_framework import serializers
from .models import ProductoModel, ServicioModel

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductoModel
        fields=(
            'id',
            'nombre',
            'serial',
            'categoria',
            'marca',
            'modelo',
            'descripcion',
            'precio',
            'stock',
            'id_proveedor'
        )
        

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServicioModel
        fields=(
            'id',
            'nombre',
            'descripcion',
            'precio'
        )