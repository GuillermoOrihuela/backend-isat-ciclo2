from rest_framework import serializers
from .models import UsuarioModel, ClienteModel, ProveedorModel
from django.contrib.auth import get_user_model
import re 



User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = UsuarioModel
        fields = (
            'id',
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
    # valida campos del formulario
    def validate_dni(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("El DNI debe tener exactamente 8 dígitos.")
        return value
    
    def validate_nombre(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("Los nombres solo puede contener letras y espacios.")
        return value
    
    def validate_password(self, value):
        if re.match(r'^[\'"]+$', value):
            if not re.match(r'^[a-zA-Z0-9\s@$!%*?&.,#_-\-\.,#]+$', value):
                raise serializers.ValidationError("El password contiene caracteres inválidos.")
            return value
    
    def validate_direccion(self, value):
        if not re.match(r'^[a-zA-Z0-9\sñÑ\-\.,#]+$', value):
            raise serializers.ValidationError("La dirección contiene caracteres inválidos.")
        return value
    
    def validate_telefono(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("El numero de contacto debe tener exactamente 9 dígitos.")
        return value

        # read_only_fields=('is_staff',)
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Encripta
        user.save()
        return user
    
class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClienteModel
        fields = (
            'id',
            'dni',
            'nombres',
            'apellidos',
            'direccion',
            'telefono',
            'email'
            )
        # read_only_fields=("id",)
    def validate_dni(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("El DNI debe tener exactamente 8 dígitos.")
        return value
    
    def validate_nombres(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("Los nombres solo puede contener letras y espacios.")
        return value
    
    def validate_apellidos(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("Los apellidos solo puede contener letras y espacios.")
        return value
    
    def validate_direccion(self, value):
        if not re.match(r'^[a-zA-Z0-9ñÑ\s\-\.,#]+$', value):
            raise serializers.ValidationError("La dirección contiene caracteres inválidos.")
        return value
    
    def validate_telefono(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("El numero de contacto debe tener exactamente 9 dígitos.")
        return value

        
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorModel
        fields = (
            'id',
            'dni',
            'nombres',
            'apellidos',
            'direccion',
            'telefono',
            'email',
            )
        # read_only_fields=('telefono',)

    def validate_dni(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("El DNI debe tener exactamente 8 dígitos.")
        return value
    
    def validate_nombres(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("Los nombres solo puede contener letras y espacios.")
        return value
    
    def validate_apellidos(self, value):
        if not re.match(r'^[a-zñ\s]+$', value):
            raise serializers.ValidationError("Los apellidos solo puede contener letras y espacios.")
        return value
    
    def validate_direccion(self, value):
        if not re.match(r'^[a-zA-Z0-9ñÑ\s\-\.,#]+$', value):
            raise serializers.ValidationError("La dirección contiene caracteres inválidos.")
        return value
    
    def validate_telefono(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("El numero de contacto debe tener exactamente 9 dígitos.")
        return value
        

        