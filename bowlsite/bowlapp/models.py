from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Leaderboard(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    date_created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name