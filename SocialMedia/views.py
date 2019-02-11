from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,GenericAPIView
# Create your views here.
from .Serializer import *
from .models import *


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostLikeCreateView(ListCreateAPIView):
    serializer_class = PostLikeSerializer

    def get_queryset(self):
        return PostLike.objects.filter(post__pk=self.kwargs['pk'])


class PostCommentCreateView(ListCreateAPIView):
    serializer_class = PostCommentSerializer

    def get_queryset(self):
        return PostComment.objects.filter(post=self.kwargs['pk'])


class PostPictureCreateView(ListCreateAPIView):
    serializer_class = PostPictureSerializer

    def get_queryset(self):
        return Post.objects.all()


class GroupCreateView(ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()


class GroupMemberCreateView(ListCreateAPIView):
    serializer_class = GroupMemberSerializer

    def get_queryset(self):
        return GroupMembers.objects.filter(group=self.kwargs['pk'])


class GroupPostCreateView(ListCreateAPIView):
    serializer_class = GroupPostSerializer

    def get_queryset(self):
        return GroupPost.objects.filter(group=self.kwargs['pk'])


