from rest_framework import serializers
from .models import UsuarioModel, ClienteModel, ProveedorModel
from django.contrib.auth import get_user_model

User = get_user_model()



class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=UsuarioModel
        fields=(
            'dni',
            'nombre' ,
            'email',
            'password',
            'direccion',
            'telefono',
            'is_active',
            'is_staff',
            'is_superuser'
        )
        # read_only_fields=('is_staff',)
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
        

        