from django.urls import path
from notifications.views import *

urlpatterns = [
    path('getnotifications/<int:pk>',GetAllNotifications.as_view())
]