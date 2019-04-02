from django.urls import path
from notifications.views import *

url_patterns = [
    path('getnotifications/<int:pk>',GetAllNotifications.as_view())
]