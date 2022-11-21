from django.contrib.auth.models import User, Group
from rest_framework import serializers
from imobiliariaSA.models import Imovel, FotoImovel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]



class FotosImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FotoImovel
        fields = ["id", "descricao", "foto"]

class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    fotos = FotosImovelSerializer(many=True, required=False, read_only=False)
    class Meta:
        model = Imovel
        fields = ["nome", "descricao", "fotos"]
