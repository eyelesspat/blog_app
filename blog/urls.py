from django.urls import path
from .views import post_list, PostListAPIView, home

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
    path('', home, name='home'),
]
