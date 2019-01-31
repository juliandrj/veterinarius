from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from modelos.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'url', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'url')

class OpcionMenuSerializer(serializers.ModelSerializer):
    opcion_padre = serializers.SlugRelatedField(many=False, read_only=True, slug_field='id')
    class Meta:
        model = OpcionMenu
        fields = ('id', 'label', 'ruta', 'grupo', 'opcion_padre')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id', 'genero')

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('id', 'especie')

class RazaSerializer(serializers.ModelSerializer):
    especie = EspecieSerializer(many=False, read_only=True)
    class Meta:
        model = Raza
        fields = ('id', 'raza', 'especie')

class MedicoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Medico
        fields = ('id', 'nuid', 'direccion', 'telefono', 'usuario', 'tarjeta_profesional', 'ruta_firma')

class PropietarioSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Propietario
        fields = ('id', 'nuid', 'direccion', 'telefono', 'usuario')

class MascotaSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer(many=False, read_only=True)
    raza = RazaSerializer(many=False, read_only=True)
    propietario = serializers.SlugRelatedField(many=False, read_only=True, slug_field='id')
    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'fecha_nacimiento', 'ruta_foto', 'genero', 'raza', 'propietario')

class AgendaSerializer(serializers.ModelSerializer):
    mascota = MascotaSerializer(many=False, read_only=True)
    fecha = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Agenda
        fields = ('id', 'mascota', 'fecha')

class AgendaESerializer(serializers.ModelSerializer):
    medico = serializers.SlugRelatedField(many=False, slug_field='id', queryset=Medico.objects.all())
    mascota = serializers.SlugRelatedField(many=False, slug_field='id', queryset=Mascota.objects.all())
    fecha = serializers.DateTimeField()
    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'mascota', 'fecha')
