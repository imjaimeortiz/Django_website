from django.db import models
import datetime
from datetime import date
from django.utils import timezone
# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=30)
    body = models.TextField()
    link = models.TextField(default="", blank=True)
    doc = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title