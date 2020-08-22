from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    routes = models.ManyToManyField('Route', related_name='stations')

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name