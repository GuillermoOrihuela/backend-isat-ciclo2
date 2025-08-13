from rest_framework import routers
from .views import ControlMantenimientoViewSet, CustodioViewSet
router=routers.DefaultRouter()
router.register('api/control', ControlMantenimientoViewSet, 'control')
router.register('api/custodio', CustodioViewSet, 'custodio')

urlpatterns=router.urls