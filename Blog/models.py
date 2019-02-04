from django.db import models
from UserHandling.models import Profile
# Create your models here.
from datetime import date




class Blog(models.Model):
    """
    Model representing a blog post.
    """
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)
    # image_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name + ' --- posted by----'+self.author.first_name


class BlogPicture(models.Model):
    picture = models.FileField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.name


class BlogLike(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)


class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because BlogComment can only have one author/User, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring
