from rest_framework.serializers import ModelSerializer
from .models import *


class NotificationSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Notification
