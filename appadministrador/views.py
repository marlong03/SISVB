from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, TipoVotacion, Plancha, Voto, Rol
from rest_framework import viewsets
from .serializers import RolSerializer,UsuarioSerializer, TipoVotacionSerializer, PlanchaSerializer, VotoSerializer

class RolViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,) 
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para el modelo TipoVotacion
class TipoVotacionViewSet(viewsets.ModelViewSet):
    queryset = TipoVotacion.objects.all()
    serializer_class = TipoVotacionSerializer

# Vista para el modelo Plancha
class PlanchaViewSet(viewsets.ModelViewSet):
    queryset = Plancha.objects.all()
    serializer_class = PlanchaSerializer

# Vista para el modelo Voto
class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer