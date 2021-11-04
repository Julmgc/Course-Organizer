from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Submissions(models.Model):
    grade = models.IntegerField(null=True)
    repo = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="submission_id")
    activity = models.ForeignKey("activities.Activities", on_delete=CASCADE, related_name="submissions")

