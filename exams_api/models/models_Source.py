from django.db import models
from rest_framework.response import Response
from rest_framework.validators import ValidationError

class Source(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=2020, blank=True)

    class Meta:
        ordering = ['name', 'year']
        unique_together = ('name', 'year',)

    def __str__(self):
        return "%s - %s" % (self.name.upper(), self.year)