from django.urls import path
from .views import *
urlpatterns = [
    path('getuserblog/<int:pk>',GetUserBlog.as_view()),
    path('editblog/<int:pk>',UpdateBlog.as_view()),
    path('createblog',BlogCreateView.as_view()),
]