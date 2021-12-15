from django.db import models
from .models_Question import *

class Alternatives(models.Model):
    orderNumber = models.PositiveSmallIntegerField(default = 0)
    isCorrect = models.BooleanField(default = False)
    question = models.ForeignKey(Question, on_delete = models.SET_NULL, null=True)

    class Meta:
        ordering = ['orderNumber']
        managed = True
    
    def save(self, *args, **kwargs):
        if not Alternatives.objects.filter(question= self.question, isCorrect = self.isCorrect):# Fonte.objects.filter():
            super().save(*args, **kwargs)
        else:
            oldAlternative = Alternatives.objects.filter(question= self.question, isCorrect = self.isCorrect).first()
            oldAlternative.isCorrect = not self.isCorrect
            oldAlternative.save()
            super().save(*args, **kwargs)
            