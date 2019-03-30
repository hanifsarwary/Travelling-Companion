from django.urls import path
from .views import *
urlpatterns = [
    path('createpost',PostCreateView.as_view()),
    path('createpostcomment/<int:pk>',PostCommentCreateView.as_view()),
    path('createpostlike/<int:pk>',PostLikeCreateView.as_view()),
    path('createpostpicture',PostPictureCreateView.as_view()),
    path('creategroup',GroupCreateView.as_view()),
    path('creategroupmember/<int:pk>',GroupMemberCreateView.as_view()),
    path('creategrouppost/<int:pk>',GroupPostCreateView.as_view()),
    path('getgroupbyid/<int:pk>',GetGroupByIdView.as_view()),
    path('getgroupbyname/<str:group_name>',GetGroupByNameView.as_view()),
    path('getpost/<int:pk>',GetPostView.as_view()),
    path('getuserpost/<str:user__username>',GetUserPost.as_view()),
    path('getuserpostbyid/<int:pk>',GetUserPostById.as_view()),
]