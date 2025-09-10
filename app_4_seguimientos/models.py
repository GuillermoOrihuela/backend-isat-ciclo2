from django.db import models
from app_1_personas.models import ClienteModel, UsuarioModel


class ControlMantenimientoModel(models.Model):
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    fecha_programada = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    id_cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)

class CustodiaModel(models.Model):
    motivo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_programada = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    id_cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    id_usuario  = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)

