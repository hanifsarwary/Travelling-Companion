from rest_framework import serializers
from .models import *
from notifications.models import *
from UserHandling.models import *


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        blog = Blog.objects.create(**validated_data)
        author = validated_data['author']
        followers = FollowerFollowing.objects.filter(followee=author)
        for fol in followers:
            noti = Notification.objects.create(notification_to=fol,notfication_text=str(author)+"created a blog with name"+validated_data["name"])
        return blog


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogComment
        fields = '__all__'

    def create(self, validated_data):
        blogcomment = BlogComment.objects.create(**validated_data)
        blog = validated_data['blog']
        comment_author = validated_data['author']
        noti = Notification.objects.create(notification_to=blog.post.author,notfication_text=comment_author.first_name+" commented on your post")
        return blogcomment


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogLike
        fields = '__all__'

    def create(self, validated_data):
        bloglike = BlogLike.objects.create(**validated_data)
        blog = validated_data['blog']
        like_author = validated_data['profile']
        noti = Notification.objects.create(notification_to=blog.post.author,notfication_text=like_author.first_name+" liked your post")
        return bloglike


class BlogEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['name','description']


class BlogPicture(serializers.ModelSerializer):

    class Meta:
        model = BlogPicture
        fields = '__all__'