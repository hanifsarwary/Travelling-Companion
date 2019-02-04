from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import hashers


class ProfileSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    def create(self, validated_data):
        validated_data['password'] = hashers.make_password((validated_data['password']))
        print(validated_data)
        return Profile.objects.create(**validated_data)


    class Meta:
        model = Profile
        fields = '__all__'

