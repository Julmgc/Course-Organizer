from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = ManyToManyField(User, related_name="courses")