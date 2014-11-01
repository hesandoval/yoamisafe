from django.db import models

# Create your models here.
class Incident(models.Model):
    longitude = models.DecimalField(max_digits=20, decimal_places=3)
    latitude = models.DecimalField(max_digits=20, decimal_places=3)
    date = models.CharField(blank=True, max_length=100)
    description = models.TextField(max_length=100)
    address = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "Description: " + self.description + " Longitude: " + str(self.longitude) + ", Latitude: " + str(self.latitude)
