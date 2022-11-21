from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from imobiliariaSA.serializers import *
from imobiliariaSA.models import Imovel, FotoImovel


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class ImovelViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows imoveis to be viewed or edited
    """

    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    permission_classes = [permissions.IsAuthenticated]

