from django.urls import path,include
from .views import *
urlpatterns = [
    path('createprofile',CreateProfileView.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('getuserbyname/<str:name>',GetUserByName.as_view()),
    path('getuserbyusername/<str:username>',GetUserByUsername.as_view())
]