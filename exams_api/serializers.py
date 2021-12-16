from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import NON_FIELD_ERRORS
from .models.models_Question import *
from .models.models_Alternatives import *
from json import dumps

class SourceSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Source
        fields = '__all__'
        
        validators = [
            UniqueTogetherValidator(
                queryset= Source.objects.all(),
                fields=['name', 'year'],
                message= "Source already exists!!!"
            )
        ]

    # def validate(self):
    #     if NON_FIELD_ERRORS:
    #         print("teste")

    # def validate_unique(self):
    #     exclude = self._get_validation_exclusions()
    #     exclude.remove('problem') # allow checking against the missing attribute

    #     try:
    #         self.instance.validate_unique(exclude=exclude)
    #     except ValidationError, e:
    #         self._update_errors(e.message_dict)

    # def validate(self, data):
    #     if Source.objects.filter(name= data["name"], year= data["year"]):
    #         dataSource = list(Source.objects.filter(name= data["name"], year= data["year"] ).values('id'))[0]
    #         print(dataSource["id"])
    #         print(dict(data)
    #         data["id"] = dataSource["id"]
    #         raise serializers.ValidationError(dict(data))
            
    #     return data
        

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