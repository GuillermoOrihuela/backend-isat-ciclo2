from rest_framework import viewsets, permissions
from .models import ProductoModel, ServicioModel
from .serializer import ProductoSerializer, ServicioSerializer
# from django.contrib.auth import get_user_model


# User = get_user_model()
# class SoloPropietarioOAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Permite si el usuario es el dueño del objeto o es admin
#         return obj == request.user or request.user.is_staff

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=ProductoModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductoSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset=ServicioModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ServicioSerializer