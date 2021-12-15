from django.db import models
from .models_Topic import *
from .models_Source import *

class Question(models.Model):
    choices_tipo = [
        (0,  'Objetiva'),
        (1,  'Discusiva'),
        (2,  'Somatória')
    ]
      
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, default=0, null=True)
    questionType = models.PositiveSmallIntegerField(
      choices=choices_tipo,
      default=0,
   ) 
    choices_course = [
        (0,  'Física')
    ]
    course = models.PositiveSmallIntegerField(
      default=0,
      choices = choices_course
   )  
    topics = models.ManyToManyField(Topic)
    
    isEdited = models.BooleanField('A questão já foi corrigida.', default=False)
    
    choices_difficulty = [
        (0,  '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5'),
        (5, '6'),
        (6, '7'),
        (7, '8'),
        (8, '9'),
        (9, '10'),
    ]

    difficulty = models.PositiveSmallIntegerField(default=5,
    choices = choices_difficulty)
    enunciation = models.TextField(blank=True)
    fig = models.ImageField(upload_to='fig/', blank=True)
    query = models.TextField(blank=True)
    additionalData = models.CharField(max_length=200, blank=True)
    resolution = models.TextField(blank=True)

    incTimeStamp = models.DateTimeField('data_inc', auto_now_add=True)
    modificationTimeStamp = models.DateTimeField('data_mod', auto_now=True)

    def __str__(self):
        return  "Question id = %s - '%s...'" % (self.id, self.enunciation)
    
    importText = models.TextField(blank=True)
    importQuery = models.TextField(blank=True)
    importResolution = models.TextField(blank=True)
    importTextFig = models.ImageField(upload_to='fig/import', blank=True)
    importQueryFig = models.ImageField(upload_to='fig/import', blank=True)
    importResolutionFig = models.ImageField(upload_to='fig/import', blank=True)

    class Meta:
        ordering = ['incTimeStamp']
        verbose_name = 'Question'
        verbose_name_plural = "Questions"
    
    def save(self, *args, **kwargs):        
        super().save(*args, **kwargs)