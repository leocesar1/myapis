from django.views.generic.base import RedirectView
from rest_framework import generics, response, status
# from .models import *
from .serializers import *
from .urls import * 
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework import permissions

# Create your views here.
class SourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data = Source.objects.filter(name= request.data["name"], year= request.data["year"]).values()[0]
            return JsonResponse(data)

        return super().create(request)

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