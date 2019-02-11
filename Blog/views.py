from django.shortcuts import render
from rest_framework.generics import UpdateAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListAPIView,ListCreateAPIView,DestroyAPIView
# Create your views here.
from .Serializer import *


class BlogCreateView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class GetBlogView(RetrieveAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(pk=self.kwargs['pk'])

class GetUserBlog(RetrieveAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(author=self.kwargs['pk'])


class UpdateBlog(UpdateAPIView):
    serializer_class = BlogEditSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


class DeleteBlog(DestroyAPIView):
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class AddBlogPicture(ListCreateAPIView):
    serializer_class = BlogPicture

    def get_queryset(self):
        Blog.objects.filter(pk=self.kwargs['blogid'])


def viewview(request):
    return render(request,'login.html')