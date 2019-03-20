from django.shortcuts import render
from rest_framework.generics import *
# Create your views here.
from .serializer import *


class CreateLuggageView(ListCreateAPIView):
    serializer_class = LuggageSerializer
    queryset = LuggageSharing.objects.all()


class GetLuggageView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = LuggageSerializer

    def get_queryset(self):
        return LuggageSharing.objects.filter(pk=self.kwargs['pk'])