
from rest_framework import viewsets, permissions, status
from .models import UsuarioModel, ClienteModel, ProveedorModel
from .serializer import UsuarioSerializer, ClienteSerializer, ProveedorSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.db import IntegrityError
from app_4_seguimientos.models import ControlMantenimientoModel, CustodiaModel
User = get_user_model()


class ClienteViewSet(viewsets.ModelViewSet):
    queryset=ClienteModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ClienteSerializer
    # def destroy(self, request, pk=None):
    #     try:
    #         cliente = self.get_object()

    #         # Eliminar relaciones manualmente
    #         CustodiaModel.objects.filter(id_cliente=cliente).delete()
    #         ControlMantenimientoModel.objects.filter(id_cliente=cliente).delete()

    #         cliente.delete()
    #         return Response({'mensaje': 'Cliente eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

    #     except ClienteModel.DoesNotExist:
    #         return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    #     except IntegrityError as e:
    #         return Response({'error': f'Restricción de integridad: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    #     except Exception as e:
    #         return Response({'error': f'Error inesperado: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class proveedorViewSet(viewsets.ModelViewSet):
    queryset=ProveedorModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProveedorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=UsuarioModel.objects.all()
    permission_classes=[permissions.IsAdminUser]
    serializer_class=UsuarioSerializer

    
    def get_queryset(self):
        # 🔍 Puedes filtrar según el usuario logueado o roles
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)
    




