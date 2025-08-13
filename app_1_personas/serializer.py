from rest_framework import serializers
from .models import UsuarioModel, ClienteModel, ProveedorModel
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=UsuarioModel
        fields=(
            'nombre' ,
            'email',
            'password',
            'direccion',
            'telefono',
            'is_staff',
            'is_active',
        )
        read_only_fields=('is_staff',)
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Encripta
        user.save()
        return user
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClienteModel
        fields=(
             'dni',
            'nombres',
            'apellidos',
            'direccion',
            'telefono',
            'email',
            )
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProveedorModel
        fields=(
             'dni',
            'nombres',
            'apellidos',
            'direccion',
            'telefono',
            'email',
            )
        # read_only_fields=('telefono',)
        

        