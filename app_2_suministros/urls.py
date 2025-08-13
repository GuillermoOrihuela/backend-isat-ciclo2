from rest_framework import routers
from .views import ProductoViewSet, ServicioViewSet

router=routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'producto')
router.register('api/servicios', ServicioViewSet, 'servicios')
urlpatterns=router.urls