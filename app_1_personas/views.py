# import pandas as pd
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser
# from django.db import transaction
# from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from .models import UsuarioModel, ClienteModel, ProveedorModel
from .serializer import UsuarioSerializer, ClienteSerializer, ProveedorSerializer
from django.contrib.auth import get_user_model

User = get_user_model()






# class ClienteCSVImportView(APIView):
#     permission_classes=[permissions.AllowAny]
#     parser_classes = [MultiPartParser]

    
#     def importar_csv(self, request):
#         # archivo = request.FILES.get('archivo')
#         archivo = pd.read_csv('L.csv')
#         if not archivo:
#             return Response({'error': 'Archivo no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             df = pd.read_csv(archivo)
#             columnas_requeridas = {'dni', 'nombres', 'apellidos', 'direccion', 'telefono', 'email'}
#             if not columnas_requeridas.issubset(df.columns):
#                 return Response({
#                 'error': f'El archivo debe contener las columnas: {", ".join(columnas_requeridas)}'
#             }, status=status.HTTP_400_BAD_REQUEST)

#             productos = [
#                 ClienteModel(
#                     dni=row['dni'],
#                     nombres=row['nombres'],
#                     apellidos=row['apellidos'],
#                     direccion=row['direccion'],
#                     telefono=row['telefono'],
#                     email=row['email']  
#                 )
#                 for _, row in df.iterrows()
#             ]
#             with transaction.atomic():
#                 ClienteModel.objects.bulk_create(productos)
#             return Response({'mensaje': f'{len(productos)} clientes importados correctamente'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# ClienteCSVImportView.importar_csv




class ClienteViewSet(viewsets.ModelViewSet):
    queryset=ClienteModel.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ClienteSerializer
    # parser_classes = [MultiPartParser]

    # @action(detail=False, methods=['post'], url_path='importar-csv')
    # def importar_csv(self, request):
    #     archivo = request.FILES.get('archivo')
    #     if not archivo:
    #         return Response({'error': 'Archivo no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         df = pd.read_csv(archivo)
    #         columnas_requeridas = {'dni', 'nombres', 'apellidos', 'direccion', 'telefono', 'email'}
    #         if not columnas_requeridas.issubset(df.columns):
    #             return Response({
    #             'error': f'El archivo debe contener las columnas: {", ".join(columnas_requeridas)}'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    #         productos = [
    #             ClienteModel(
    #                 dni=row['dni'],
    #                 nombres=row['nombres'],
    #                 apellidos=row['apellidos'],
    #                 direccion=row['direccion'],
    #                 telefono=row['telefono'],
    #                 email=row['email']  
    #             )
    #             for _, row in df.iterrows()
    #         ]
    #         with transaction.atomic():
    #             ClienteModel.objects.bulk_create(productos)
    #         return Response({'mensaje': f'{len(productos)} clientes importados correctamente'}, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
    




