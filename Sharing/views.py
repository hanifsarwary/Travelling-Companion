from django.shortcuts import render
from rest_framework.generics import *
# Create your views here.
from .serializer import *


class CreateLuggageView(ListCreateAPIView):
    serializer_class = LuggageSerializer
    queryset = LuggageSharing.objects.all()


class GetAllLuggageView(ListAPIView):
    serializer_class = LuggageSerializer

    def get_queryset(self):
        return LuggageSharing.objects.filter(active=True)


class GetOneLuggageView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LuggageSerializer

    def get_queryset(self):
        return LuggageSharing.objects.filter(pk=self.kwargs['pk'])


class UpdateLuggageView(RetrieveUpdateAPIView):
    serializer_class = LuggageSerializer
    lookup_field = 'pk'


class CreateCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = CarSharing.objects.all()


class GetAllCarView(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = CarSharing.objects.filter(active=True)


class GetOneCarView(RetrieveAPIView):

    serializer_class = CarSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return CarSharing.objects.filter(pk=self.kwargs['pk'])


