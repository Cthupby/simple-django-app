from django.urls import include, path
from rest_framework import routers
from drf_blog import views


urlpatterns = [
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<1nt:pk>/vote', views.VoteCreate.as_view())    
]

