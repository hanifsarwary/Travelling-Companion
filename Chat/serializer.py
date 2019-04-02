from rest_framework import serializers
from .models import Dialog, Message
from notifications.models import *



class DialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        dialog = validated_data['dialog']
        owner = dialog.owner
        opponent = dialog.opponent
        if validated_data['sender'] == owner:
            noti = Notification.objects.create(notification_to=opponent,notfication_text=str(owner)+"sent you a message")
        else:
            noti = Notification.objects.create(notification_to=owner,
                                               notfication_text=str(opponent) + "sent you a message")
        return message



class MessageSeenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['read']