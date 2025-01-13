from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, TipoVotacion, Plancha, Voto, Rol
from rest_framework import viewsets
from .serializers import RolSerializer,UsuarioSerializer, TipoVotacionSerializer, PlanchaSerializer, VotoSerializer


from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class RolViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class LoginView(APIView):
    """
    Vista para el login de usuarios
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Autenticar al usuario
        user = authenticate(username=username, password=password)
        if user is not None:
            # Crear o recuperar el token del usuario
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Credenciales inválidas. Verifica tu usuario y contraseña.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

class LogoutView(APIView):
    """
    Vista para el logout de usuarios
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Eliminar el token existente
            token = Token.objects.get(user=request.user)
            token.delete()

            return Response(
                {'message': 'Sesión cerrada exitosamente.'},
                status=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return Response(
                {'error': 'El usuario no tiene un token válido.'},
                status=status.HTTP_400_BAD_REQUEST
            )

def get_user_from_token(request):
    token = request.headers.get('Authorization')
    if not token:
        raise AuthenticationFailed('Authorization token is missing')
    
    try:
        token = token.split(' ')[1]  # 'Bearer <token>'
        decoded_token = AccessToken(token)  # Asumiendo que AccessToken es de alguna librería como SimpleJWT
        user_id = decoded_token['user_id']
        user = User.objects.get(id=user_id)
        return user
    except Exception as e:
        raise AuthenticationFailed('Invalid or expired token')

class UserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = get_user_from_token(request)
            return JsonResponse({'username': user.username, 'email': user.email})
        except AuthenticationFailed:
            return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para el modelo TipoVotacion
class TipoVotacionViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,) 

    queryset = TipoVotacion.objects.all()
    serializer_class = TipoVotacionSerializer

# Vista para el modelo Plancha
class PlanchaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    
    queryset = Plancha.objects.all()
    serializer_class = PlanchaSerializer

# Vista para el modelo Voto
class VotoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer