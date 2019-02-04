from django.urls import path,include
from .views import *
urlpatterns = [
    path('createprofile',CreateProfileView.as_view()),
    path('auth/', include('rest_auth.urls')),
]