from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    choices_topicTypes = [
        (0,  'Secundário'),
        (1,  'Primário'  ),
     ]
    topicType = models.PositiveSmallIntegerField(choices = choices_topicTypes, default = 0) 

    class Meta:
        ordering = ['name', 'topicType']
        managed = True
    
    def save(self, *args, **kwargs):
        if not Topic.objects.filter(nome= self.name, tipo= self.topicType ):# Fonte.objects.filter():
            super().save(*args, **kwargs)
        else:
            return "This topic is already in database."
    
    def __str__(self):
        return "%s (%s)" % (self.name, self.topicType)