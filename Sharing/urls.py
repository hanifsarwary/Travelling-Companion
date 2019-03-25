from django.urls import path
from .views import *
urlpatterns = [
    path('createluggage',CreateLuggageView.as_view()),
    path('getluggage/<int:pk>',GetOneLuggageView.as_view())
]