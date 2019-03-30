from django.db import models
from UserHandling.models import Profile
# Create your models here.
from Search.models import Location


class CarSharing(models.Model):
    choices = (
        ('lhr', 'Lahore'),
        ('fsd', 'Faisalabad'),
        ('isb', 'Islamabad'),
    )
    posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    capacity = models.PositiveIntegerField(default=1)
    source_location = models.CharField(choices=choices,max_length=15)
    dest_location = models.CharField(choices=choices,max_length=15)
    car_model = models.CharField(max_length=20)
    car_number = models.CharField(max_length=15)

    def __str__(self):
        return "request for car sharing is posted by "+self.posted_by.__str__()


class LuggageSharing(models.Model):
    choices = (
        ('lhr', 'Lahore'),
        ('fsd', 'Faisalabad'),
        ('isb', 'Islamabad'),
    )
    posted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    capacity = models.PositiveIntegerField(default=1)
    source_location = models.CharField(choices=choices, max_length=15)
    dest_location = models.CharField(choices=choices, max_length=15)

    def __str__(self):
        return "request for Luggage Sharing is posted by " + self.posted_by.__str__()


class CarSharingAcceptance(models.Model):
    accepted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    carsharing = models.ForeignKey(CarSharing,on_delete=models.CASCADE)
    count = models.IntegerField(default=1)


class LuggageSharingAcceptance(models.Model):
    accepted_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    luggageSharing = models.ForeignKey(LuggageSharing,on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

