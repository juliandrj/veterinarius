from django.contrib.auth.models import User, Group
from modelos.models import *
from rest_framework import viewsets, permissions, generics
from api.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class OpcionMenuViewSet(viewsets.ModelViewSet):
    queryset = OpcionMenu.objects.all()
    serializer_class = OpcionMenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = OpcionMenu.objects.all()
    serializer_class = OpcionMenuSerializer
    def get_queryset(self):
        id_grupos = []
        for g in self.request.user.groups.all():
            id_grupos.append(g.pk)
        queryset = OpcionMenu.objects.filter(grupo_id__in=id_grupos).order_by('opcion_padre','pk')
        return queryset

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    def get_queryset(self):
        queryset = Mascota.objects.all()
        propietarioId = self.request.query_params.get('propietario', None)
        if propietarioId is not None:
            queryset = Mascota.objects.filter(propietario_id=propietarioId).order_by('nombre')
        return queryset

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    def get_queryset(self):
        queryset = Agenda.objects.all()
        medicoId = self.request.query_params.get('medico', None)
        if medicoId is not None:
            queryset = Agenda.objects.filter(medico_id=medicoId).order_by('fecha')
        return queryset
