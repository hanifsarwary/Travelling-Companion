from django.urls import path,include
from .views import *
urlpatterns = [
    path('getuserblog/<int:pk>',GetUserBlog.as_view()),
    path('editblog/<int:pk>',UpdateBlog.as_view()),
    path('createblog',BlogCreateView.as_view()),
    path('deleteblog/<int:pk>', DeleteBlog.as_view()),
    path('addpicture/<int:blogid>',AddBlogPicture.as_view()),


]