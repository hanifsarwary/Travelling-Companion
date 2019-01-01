from django.db import models
from UserHandling.models import Profile
# Create your models here.


class Question(models.Model):
    statement = models.CharField(max_length=350)
    rating = models.FloatField(default=0)
    asked_by = models.ForeignKey(Profile,on_delete=models.CASCADE)


class Answers(models.Model):
    statement = models.CharField(max_length=1000)
    upvote = models.PositiveIntegerField(default=0)
    answered_by = models.ForeignKey(Profile,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)


class Location(models.Model):
    location_name = models.CharField(max_length=120)
    longitude = models.FloatField()
    latitude = models.FloatField()




