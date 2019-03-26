from django.shortcuts import render
from .Serializer import *
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView
from django.views import View
# Create your views here.
from django.http import JsonResponse


class CreateProfileView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class GetAllUserView(RetrieveAPIView):
    serializer_class = ProfileSendSerializer

    def get_queryset(self):
        return Profile.objects.all()


class GetUserCountView(View):

    def get(self,request):
        count = Profile.objects.all().count()
        data = {
             'count': count}

        return JsonResponse(data)


class GetSingleUser(RetrieveAPIView):

    serializer_class = ProfileSendSerializer

    def get_queryset(self):
        return Profile.objects.filter(pk=self.kwargs['pk'])


class GetUserByName(RetrieveAPIView):

    serializer_class = ProfileSendSerializer
    lookup_field = 'first_name'

    def get_queryset(self):
        return Profile.objects.filter(first_name__contains=self.kwargs['first_name'])


class GetUserByUsername(RetrieveAPIView):

    serializer_class = ProfileSendSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return Profile.objects.filter(username=self.kwargs['username'])