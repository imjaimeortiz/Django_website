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
    language = models.TextField(null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def has_link(self):
        if self.link != "":
            return True
        else :
            return False
    
    def has_doc(self):
        if self.doc != "":
            return True
        else :
            return False