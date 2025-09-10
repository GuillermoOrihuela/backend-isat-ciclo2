from rest_framework import serializers
from .models import ControlMantenimientoModel, CustodiaModel
import re

class ControlMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ControlMantenimientoModel
        fields=(
            'id',
            'tipo',
            'descripcion',
            'fecha_programada',
            'id_cliente',
        )
class CustodioSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustodiaModel
        fields=(
            'id',
            'motivo',
            'tipo',
            'marca',
            'modelo',
            'descripcion' ,
            'fecha_programada',
            'id_cliente',
            'id_usuario'
        )

    def validate_motivo(self, value):
        if not re.match(r'^[a-z0-9\sñ\-\.,#]+$', value):
            raise serializers.ValidationError("el nombre de producto solo puede contener letras y espacios.")
        return value
    
    def validate_tipo(self, value):
        if not re.match(r'^[a-z0-9\sñ\-\.,#]+$', value):
            raise serializers.ValidationError("el tipo de producto solo puede contener letras y espacios.")
        return value
    
    def validate_marca(self, value):
        if not re.match(r'^[a-zA-Z0-9\s\-\.,#]+$', value):
            raise serializers.ValidationError("La marca contiene caracteres inválidos.")
        return value
    
    def validate_modelo(self, value):
        if not re.match(r'^[a-zA-Z0-9\s\-\.,#]+$', value):
            raise serializers.ValidationError("El modelo contiene caracteres inválidos.")
        return value
    
    def validate_descripcion(self, value):
        if not re.match(r'^[a-zA-Z0-9\s\-\.,#]+$', value):
            raise serializers.ValidationError("La descripcion contiene caracteres inválidos.")
        return value