from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class LikedPlaces(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    places = models.IntegerField()