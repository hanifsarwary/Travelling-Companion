from django.shortcuts import render
from .Serializer import *
from rest_framework.generics import CreateAPIView,ListCreateAPIView

# Create your views here.


class CreateProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
