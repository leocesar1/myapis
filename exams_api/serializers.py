from rest_framework import serializers
from .models.models_Question import *
from .models.models_Alternatives import *

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AlternativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternatives
        fields = '__all__'