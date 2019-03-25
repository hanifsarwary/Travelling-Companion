from rest_framework import serializers
from .models import Dialog, Message


class DialogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dialog
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class MessageSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['read']