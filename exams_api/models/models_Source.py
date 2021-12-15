from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=2020, blank=True)

    class Meta:
        ordering = ['name', 'year']
    
    def save(self, *args, **kwargs):
        if not Source.objects.filter(name= self.name, year= self.year ):
            super().save(*args, **kwargs)
        else:
            return "This source is already in the database."

    def __str__(self):
        return "%s - %s" % (self.name.upper(), self.year)