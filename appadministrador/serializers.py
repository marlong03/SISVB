from rest_framework import serializers
from .models import Usuario, TipoVotacion, Plancha, Voto, Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

from .models import Usuario, TipoVotacion, Plancha, Voto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'document_number', 'id_rol','email', 'password', 'is_active', 'date_created', 'date_modified']

class TipoVotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVotacion
        fields = ['id', 'name', 'description', 'number_votes', 'date_created', 'date_modified','state','date_start','date_end']

class PlanchaSerializer(serializers.ModelSerializer):
    id_tipovotacion = TipoVotacionSerializer(read_only=True)

    class Meta:
        model = Plancha
        #fields = ['id', 'name', 'description', 'image', 'state', 'date_created', 'date_modified', 'id_tipovotacion']
        fields = '__all__'

class VotoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    id_tipovotacion = TipoVotacionSerializer(read_only=True)
    id_plancha = PlanchaSerializer(read_only=True)

    class Meta:
        model = Voto
        fields = ['id', 'usuario', 'id_tipovotacion', 'id_plancha', 'date_created', 'date_modified']
