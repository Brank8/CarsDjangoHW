from django.db import models
from django.urls import reverse
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})