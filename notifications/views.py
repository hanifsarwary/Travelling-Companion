from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from notifications.Serializer import NotificationSerializer
from notifications.models import *

class GetAllNotifications(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(notification_to=self.kwargs['pk'])