from django.contrib.auth.models import User, Group
from modelos.models import OpcionMenu
from rest_framework import viewsets, permissions, generics
from api.serializers import UserSerializer, GroupSerializer, OpcionMenuSerializer

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
        queryset = OpcionMenu.objects.filter(pk__in=id_grupos)
        return queryset
