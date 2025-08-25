from rest_framework import viewsets, permissions
from .models import CustodiaModel, ControlMantenimientoModel
from .serializer import CustodioSerializer, ControlMantenimientoSerializer
# from django.contrib.auth import get_user_model


# User = get_user_model()
# class SoloPropietarioOAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Permite si el usuario es el dueño del objeto o es admin
#         return obj == request.user or request.user.is_staff

class ControlMantenimientoViewSet(viewsets.ModelViewSet):
    queryset=ControlMantenimientoModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ControlMantenimientoSerializer

class CustodioViewSet(viewsets.ModelViewSet):
    queryset=CustodiaModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CustodioSerializer


