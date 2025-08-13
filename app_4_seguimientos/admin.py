from django.contrib import admin
from .models import CustodiaModel, ControlMantenimientoModel
# Register your models here.


class CustodiaAdmin(admin.ModelAdmin):
    list_display=('motivo', 'fecha_programada', 'id_cliente', 'id_usuario')
    search_fields=('motivo', 'fecha_programada', 'id_cliente', 'id_usuario')
admin.site.register(CustodiaModel, CustodiaAdmin)


class ControlManenimientoAdmin(admin.ModelAdmin):
    list_display=('id', 'tipo', 'fecha_programada', 'id_cliente')
    serch_fields=('id', 'tipo', 'fecha_programada', 'id_cliente')
admin.site.register(ControlMantenimientoModel, ControlManenimientoAdmin)