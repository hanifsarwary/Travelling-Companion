from django.db import models
from UserHandling.models import Profile
# Create your models here.


class Post(models.Model):
    post_text = models.CharField(max_length=1500)
    post_date = models.DateField()
    post_time = models.TimeField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)



class PostPicture(models.Model):
    picture = models.FileField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)




class PostLike(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class PostComment(models.Model):

    comment_text = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):

        len_title = 75
        if len(self.comment_text) > len_title:
            titlestring = self.comment_text[:len_title] + '...'
        else:
            titlestring = self.comment_text
        return titlestring


class Group(models.Model):
    group_admin = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    group_name = models.CharField(max_length=50)
    date_created = models.DateField()
    time_created = models.TimeField()


class GroupMembers(models.Model):
    member = models.ForeignKey(Profile,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)


class GroupPost(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)