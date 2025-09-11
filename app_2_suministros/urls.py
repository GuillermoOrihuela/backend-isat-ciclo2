from rest_framework import routers
from .views import ProductoViewSet, ServicioViewSet

router=routers.DefaultRouter()
router.register('api/productos', ProductoViewSet)
router.register('api/servicios', ServicioViewSet)
urlpatterns=router.urls
