from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('gardens_api/local/<int:pk>/', views.LocalUpdate.as_view(), name='local-update'),
    url(r'^gardens_api/local/$', views.LocalList.as_view(), name='local-list'),

    path('gardens_api/actuator/<int:pk>/', views.ActuatorUpdate.as_view(), name='actuator-update'),
    url(r'^gardens_api/actuator/$', views.ActuatorList.as_view(), name='actuator-list'),

    path('gardens_api/sensor/<int:pk>/', views.SensorUpdate.as_view(), name='sensor-update'),
    path('gardens_api/sensor/', views.SensorList.as_view(), name='sensor-list'),

    path('gardens_api/data_sensor/<int:pk>/', views.DataSensorUpdate.as_view(), name='datasensor-update'),
    url(r'^gardens_api/data_sensor/$', views.DataSensorList.as_view(), name='datasensor-list'),
]