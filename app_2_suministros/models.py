from django.db import models
from app_1_personas.models import ProveedorModel

class ProductoModel(models.Model):
    nombre = models.CharField(max_length=50)
    serial = models.CharField(max_length=10) # EN PRODUCCION AUMENTAR UNIQUE
    categoria = models.CharField(max_length=20, null=True, blank=True)
    marca = models.CharField(max_length=20, null=True, blank=True)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    id_proveedor = models.ForeignKey(ProveedorModel, on_delete=models.CASCADE)
    

class ServicioModel(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
