from rest_framework import serializers
from .models import *

class FonteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonte
        fields = '__all__'

class AssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = '__all__'

class TipoAssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAssunto
        fields = '__all__'

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questao
        fields = '__all__'

class AlternativasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativas
        fields = '__all__'