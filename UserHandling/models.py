from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    profile_pic = models.FileField(upload_to='profile pictures',null=True,blank=True)
    average_rating = models.FloatField(default=0,blank=True,null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.",null=True,blank=True)

# class FollowerFollowing(models.Model):
#     followee = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='followee')
#     follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='follower'
#                                  )
#
#     class Meta:
#         unique_together = ('follower','followee')