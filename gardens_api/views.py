from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class LocalList(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class ActuatorList(generics.ListCreateAPIView):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

class ActuatorUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class DataSensorList(generics.ListCreateAPIView):
    queryset = DataSensor.objects.all()
    serializer_class = DataSensorSerializer

class DataSensorUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSensor.objects.all()
    serializer_class = DataSensorSerializer