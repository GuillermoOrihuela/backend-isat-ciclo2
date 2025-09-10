from rest_framework import serializers
from .models import ProductoModel, ServicioModel
import re

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
    
    def validate_nombre(self, value):
        if not re.match(r'^[a-zA-Z0-9\sñÑ]+$', value):
            raise serializers.ValidationError("el nombre de producto solo puede contener letras y espacios.")
        return value
    
    def validate_serial(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("La serie debe tener exactamente 10 dígitos.")
        return value
    
    def validate_categoria(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("la categorias solo puede contener letras y espacios.")
        return value
    
    def validate_marca(self, value):
        if not re.match(r'^[a-z0-9\s\-\.,#]+$', value):
            raise serializers.ValidationError("La marca contiene caracteres inválidos.")
        return value
    
    def validate_modelo(self, value):
        if not re.match(r'^[a-z0-9\s\-\.,#]+$', value):
            raise serializers.ValidationError("El modelo contiene caracteres inválidos.")
        return value
    
    def validate_descripcion(self, value):
        if not re.match(r'^[a-zA-Z0-9\sñÑ\-\.,#]+$', value):
            raise serializers.ValidationError("La descripcion contiene caracteres inválidos.")
        return value
        

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServicioModel
        fields=(
            'id',
            'nombre',
            'descripcion',
            'precio'
        )

    def validate_nombre(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("el nombre de producto solo puede contener letras y espacios.")
        return value

    def validate_descripcion(self, value):
        if not re.match(r'^[a-zA-Z0-9ñÑ\s\-\.,#]+$', value):
            raise serializers.ValidationError("La descripcion contiene caracteres inválidos.")
        return value