from rest_framework import serializers
from .models import ControlMantenimientoModel, CustodiaModel


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
