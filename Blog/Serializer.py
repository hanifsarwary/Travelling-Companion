from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__' 


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogComment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogLike
        fields = '__all__'


class BlogEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['description']