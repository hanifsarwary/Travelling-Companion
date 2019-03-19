from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    profile_pic = models.FileField(upload_to='profile pictures',null=True,blank=True)
    average_rating = models.FloatField(default=0)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.")


class FollowerFollowing(models.Model):
    followee = models.ForeignKey(Profile,on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower','followee')