from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.conf import settings

class Movie(models.Model):
    name = models.CharField(max_length=100)


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
