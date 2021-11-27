from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.fields import BLANK_CHOICE_DASH


User = get_user_model()


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.movie.name


class PromoCode(models.Model):
    code = models.CharField(max_length=120)
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    usedTimes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.code


class Bookings(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    show = models.ForeignKey(
        Show, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.movie.name if self.movie.name else ""


class Seat(models.Model):
    number = models.IntegerField()
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    isBooked = models.BooleanField(default=False)

    def __str__(self):
        return "{},{}".format(self.number, self.show.movie.name)



