from django.db import models
from django.db.models.expressions import Value

choices_type = [
      (False,  'Analógico - PWM'),
      (True, 'Digital')
    ]

class Local(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not Local.objects.filter(name= self.name):
            super().save(*args, **kwargs)
        else:
            pass

    def __str__(self):
        return "%s" % (self.name)

class Actuator(models.Model):
    name = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=0)
    isDigital = models.BooleanField(
      choices=choices_type,
      default=True,
   ) 

    def __str__(self):
        return "Actuator %s - %s" % (self.name, self.local)

    class Meta:
        ordering = ['name']
    
    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=0)
    isDigital = models.BooleanField(
      choices=choices_type,
      default=True,
   ) 

    def __str__(self):
        return "Sensor %s - %s" % (self.name, self.local)

    class Meta:
        ordering = ['name']
    
    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)


class DataSensor(models.Model):
    datetime = models.DateTimeField('datatime', auto_now_add=True)
    valueSensor = models.FloatField('value')
    sensorId = models.ForeignKey(Sensor, on_delete=models.CASCADE)