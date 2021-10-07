from django.db import models
from django.db.models.base import Model
from django.core.files.images import get_image_dimensions

# Create your models here.
class Shooting(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField(max_length=50)
    photographer = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    # This function checks if the image has more height or width
    def tall_shooting(self):
        width, height = get_image_dimensions(self.image)
        if width > height:
            return False
        else:
            return True