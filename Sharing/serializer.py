from rest_framework import serializers
from .models import *


class LuggageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LuggageSharing
        fields = '__all__'