
from rest_framework import viewsets, permissions, status
from .models import UsuarioModel, ClienteModel, ProveedorModel
from .serializer import UsuarioSerializer, ClienteSerializer, ProveedorSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# from django.db import IntegrityError
# from app_4_seguimientos.models import ControlMantenimientoModel, CustodiaModel

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken





User = get_user_model()



class ClienteViewSet(viewsets.ModelViewSet):
    queryset=ClienteModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ClienteSerializer

class proveedorViewSet(viewsets.ModelViewSet):
    queryset=ProveedorModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProveedorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=UsuarioModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=UsuarioSerializer

    @action(detail=False, methods=["post"])
    def logout(self, request):
        """
        Invalida el refresh token (logout).
        """
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  #  invalida el refresh token
            return Response(
                {"message": "Sesión cerrada correctamente."},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": "Token inválido o ya caducado."},
                status=status.HTTP_400_BAD_REQUEST
            )

    
    def get_queryset(self):
        # 🔍 Puedes filtrar según el usuario logueado o roles
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
    
    
    




