from django.contrib.auth.models import User, Group
from rest_framework import serializers
from modelos.models import OpcionMenu

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
