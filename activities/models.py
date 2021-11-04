from django.db import models
from django.contrib.auth.models import User

class Activities(models.Model):
    title = models.CharField(max_length=255, unique=True)
    points = models.IntegerField()
   
