from rest_framework import viewsets, permissions
from .models import UsuarioModel, ClienteModel, ProveedorModel
from .serializer import UsuarioSerializer, ClienteSerializer, ProveedorSerializer
from django.contrib.auth.models import User





class SoloPropietarioOAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite si el usuario es el dueño del objeto o es admin
        return obj == request.user or request.user.is_staff

class ClienteViewSet(viewsets.ModelViewSet):
    queryset=ClienteModel.objects.all()
    permission_classes=[SoloPropietarioOAdmin]
    serializer_class=ClienteSerializer

class proveedorViewSet(viewsets.ModelViewSet):
    queryset=ProveedorModel.objects.all()
    permission_classes=[SoloPropietarioOAdmin]
    serializer_class=ProveedorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=UsuarioModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=UsuarioSerializer
    def get_queryset(self):
        # 🔍 Puedes filtrar según el usuario logueado o roles
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
    




