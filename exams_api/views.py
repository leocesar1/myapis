from rest_framework import generics
from .models import *
from .serializers import AlternativasSerializer, AssuntoSerializer, FonteSerializer, QuestaoSerializer, TipoAssuntoSerializer

# Create your views here.
class FonteList(generics.ListCreateAPIView):
    queryset = Fonte.objects.all()
    serializer_class = FonteSerializer

class FonteUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fonte.objects.all()
    serializer_class = FonteSerializer

class AssuntoList(generics.ListCreateAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer

class AssuntoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer

class TipoAssuntoList(generics.ListCreateAPIView):
    queryset = TipoAssunto.objects.all()
    serializer_class = TipoAssuntoSerializer

class QuestaoList(generics.ListCreateAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

class QuestaoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer

class AlternativasList(generics.ListCreateAPIView):
    queryset = Alternativas.objects.all()
    serializer_class = AlternativasSerializer

class AlternativasUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alternativas.objects.all()
    serializer_class = AlternativasSerializer