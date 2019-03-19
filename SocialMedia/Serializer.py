from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


# class PostPictureSerializer(ModelSerializer):
#
#     class Meta:
#         model = PostPicture
#         fields = '__all__'


class PostLikeSerializer(ModelSerializer):

    class Meta:
        model = PostLike
        fields = '__all__'


class PostCommentSerializer(ModelSerializer):

    class Meta:
        model = PostComment
        fields = '__all__'


class GroupSerializer(ModelSerializer):

    class Meta:

        model = Group
        fields = '__all__'


class GroupMemberSerializer(ModelSerializer):

    class Meta:

        model = GroupMembers
        fields = '__all__'


class GroupPostSerializer(ModelSerializer):

    class Meta:

        model = GroupPost
        fields = '__all__'