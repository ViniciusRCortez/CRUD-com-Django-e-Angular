from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, authentication
from imobiliariaSA.serializers import *
from imobiliariaSA.models import *

#Para pedir token de autenticação
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
import json

@csrf_exempt
def login(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    if body["username"]:
        user = authenticate(username=body["username"], password=body["password"])
        if user:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse({"token" : token[0].key, "id" : user.id, "usuario" : user.username, "email" : user.email, "nome" : user.first_name})

class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,]

class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [authentication.TokenAuthentication,]


class CategoriaViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [authentication.TokenAuthentication,]


class TipoImovelViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited
    """

    queryset = TipoImovel.objects.all()
    serializer_class = TipoImovelSerializer
    authentication_classes = [authentication.TokenAuthentication,]



class ImovelViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows imoveis to be viewed or edited
    """

    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    authentication_classes = [authentication.TokenAuthentication,]

