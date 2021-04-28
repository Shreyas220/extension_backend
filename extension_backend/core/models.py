from django.db import models

# Create your models here.


class timespent(models.Model):
    url = models.CharField()
    timepassed =  models.IntegerField(blank=True, null=True)

def __str__(self):
    return self.title

    