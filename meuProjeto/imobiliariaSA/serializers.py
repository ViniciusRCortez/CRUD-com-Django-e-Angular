from django.contrib.auth.models import User, Group
from rest_framework import serializers
from imobiliariaSA.models import Imovel, FotoImovel, TipoImovel, Categoria

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]



class FotosImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoImovel
        fields = ["id", "descricao", "foto"]

class ImovelSerializer(serializers.ModelSerializer):
    fotos = FotosImovelSerializer(many=True, required=False, read_only=False)
    class Meta:
        model = Imovel
        fields = ["nome", "descricao", "fotos", "categoria", "tipoImovel"]

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "status"]


class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoImovel
        fields = ["id", "nome", "status"]
