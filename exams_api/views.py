from rest_framework import generics
# from .models import *
from .serializers import *

from rest_framework import permissions

# Create your views here.
class SourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class SourceUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class TopicList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class QuestionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AlternativesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Alternatives.objects.all()
    serializer_class = AlternativesSerializer

class AlternativesUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Alternatives.objects.all()
    serializer_class = AlternativesSerializer