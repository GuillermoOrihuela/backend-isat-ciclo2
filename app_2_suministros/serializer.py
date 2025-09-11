from rest_framework import serializers
from .models import ProductoModel, ServicioModel, ImagenModel
import re, json




class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenModel
        fields=['id', 'imagen']

class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, read_only=True)
    nuevas_imagenes = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = ProductoModel
        fields = [
            'id', 'nombre', 'serial', 'categoria', 'marca', 'modelo',
            'descripcion', 'precio', 'stock', 'id_proveedor',
            'imagenes', 'nuevas_imagenes', 'fecha_creacion', 'fecha_modificacion'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_modificacion']

    def create(self, validated_data):
        nuevas_imagenes = validated_data.pop('nuevas_imagenes', [])
        producto = ProductoModel.objects.create(**validated_data)
        for imagen in nuevas_imagenes:
            ImagenModel.objects.create(producto=producto, imagen=imagen)
        return producto

    def update(self, instance, validated_data):
        nuevas_imagenes = validated_data.pop('nuevas_imagenes', [])
        imagenes_a_eliminar = self.context['request'].data.get('imagenes_a_eliminar')

        # Actualizar campos del producto
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Eliminar imágenes si se especifican
        if imagenes_a_eliminar:
            try:
                ids = json.loads(imagenes_a_eliminar)
                ImagenModel.objects.filter(id__in=ids, producto=instance).delete()
            except Exception as e:
                raise serializers.ValidationError(f"Error al eliminar imágenes: {str(e)}")

        # Agregar nuevas imágenes
        for imagen in nuevas_imagenes:
            ImagenModel.objects.create(producto=instance, imagen=imagen)

        return instance



    
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