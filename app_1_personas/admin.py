from django.contrib import admin
from .models import UsuarioModel, ClienteModel, ProveedorModel


class ClienteAdmin(admin.ModelAdmin):
    list_display=('dni', 'nombres', 'apellidos', 'telefono')
    search_fields=('dni', 'nombres', 'apellidos', 'telefono')
admin.site.register(ClienteModel,ClienteAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display=('dni', 'nombres', 'apellidos', 'telefono')
    search_fields=('dni', 'nombres', 'apellidos', 'telefono')
admin.site.register(ProveedorModel,ProveedorAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('dni', 'nombre', 'email')
    search_fields=('dni', 'nombre', 'email')
    list_filter = ('is_active', 'is_staff')
admin.site.register(UsuarioModel,UsuarioAdmin)


