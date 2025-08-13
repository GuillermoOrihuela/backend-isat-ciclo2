from django.contrib import admin
from .models import ProductoModel, ServicioModel
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre', 'serial', 'id_proveedor')
    search_fields=('id', 'nombre', 'serial', 'id_proveedor')
    
admin.site.register(ProductoModel, ProductoAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre', 'precio')
    search_fields=('id', 'nombre', 'precio')
    
admin.site.register(ServicioModel, ServicioAdmin)