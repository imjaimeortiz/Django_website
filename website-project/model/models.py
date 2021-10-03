from django.db import models
from django.db.models.base import Model

# Create your models here.
class Shooting(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField(max_length=50)
    photographer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title