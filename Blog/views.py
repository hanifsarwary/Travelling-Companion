from django.shortcuts import render
from rest_framework.generics import UpdateAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListAPIView,ListCreateAPIView,DestroyAPIView
# Create your views here.
from .Serializer import *


class BlogCreateView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class GetUserBlog(RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


class UpdateBlog(UpdateAPIView):
    serializer_class = BlogEditSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


class DeleteBlog(DestroyAPIView):
    serializer_class = BlogSerializer
    lookup_field = 'pk'


