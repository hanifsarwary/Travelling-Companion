from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    profile_pic = models.FileField(upload_to='profile pictures',null=True,blank=True)
    average_rating = models.FloatField(default=0)
    followers = models.ManyToManyField("self",blank=True,through='FollowerFollowee')
    following = models.ManyToManyField("self", blank=True,through='FollowerFollowee')
    number_of_followers = models.PositiveIntegerField(default=0)
    number_of_followings = models.PositiveIntegerField(default=0)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")


class FollowerFollowee(models.Model):
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE)
    followee = models.ForeignKey(Profile,on_delete=models.CASCADE)