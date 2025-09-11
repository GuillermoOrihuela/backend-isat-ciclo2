from rest_framework import viewsets, permissions
from .models import ProductoModel, ServicioModel
from .serializer import ProductoSerializer, ServicioSerializer
# from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser, FormParser


# User = get_user_model()
# class SoloPropietarioOAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Permite si el usuario es el dueño del objeto o es admin
#         return obj == request.user or request.user.is_staff

# from rest_framework.response import Response

# def update(self, request, *args, **kwargs):
#     instance = self.get_object()
#     data = request.data.copy()

#     # Preserva fecha_creacion si no se envía
#     if 'fecha_creacion' not in data:
#         data['fecha_creacion'] = instance.fecha_creacion.isoformat()

#     serializer = self.get_serializer(instance, data=data)
#     serializer.is_valid(raise_exception=True)
#     self.perform_update(serializer)
#     return Response(serializer.data)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset=ProductoModel.objects.all()
    serializer_class = ProductoSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    


class ServicioViewSet(viewsets.ModelViewSet):
    queryset=ServicioModel.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ServicioSerializer