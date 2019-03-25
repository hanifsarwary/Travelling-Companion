from rest_framework import serializers
from .models import *


class LuggageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LuggageSharing
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarSharing
        fields = '__all__'

