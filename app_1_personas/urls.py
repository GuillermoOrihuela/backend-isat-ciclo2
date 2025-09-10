from rest_framework import routers
from .views import UsuarioViewSet, ClienteViewSet, proveedorViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





router=routers.DefaultRouter()
router.register('api/usuarios', UsuarioViewSet, 'usuarios')
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/proveedores', proveedorViewSet, 'proveedores')

urlpatterns=[
    # path('','importar-csv/', ClienteCSVImportView.as_view(), name='importar-clientes-csv'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]



   