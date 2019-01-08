from django.db import models
from UserHandling.models import Profile
# Create your models here.
from Search.models import Location


class Service(models.Model):
    posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class CarSharing(Service):
    choices = (
        ('lhr','Lahore'),
        ('fsd','Faisalabad'),
        ('isb','Islamabad'),
    )
    capacity = models.PositiveIntegerField(default=1)
    source_location = models.CharField(choices=choices,max_length=15)
    dest_location = models.CharField(choices=choices,max_length=15)
    car_model = models.CharField(max_length=20)
    car_number = models.CharField(max_length=15)


class LuggageSharing(Service):
    choices = (
        ('lhr','Lahore'),
        ('fsd','Faisalabad'),
        ('isb','Islamabad'),
    )

    capacity = models.PositiveIntegerField(default=1)
    source_location = models.CharField(choices=choices, max_length=15)
    dest_location = models.CharField(choices=choices, max_length=15)

