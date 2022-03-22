from django.urls import include, path
from rest_framework import routers
from drf_blog import views


urlpatterns = [
    path('api/posts', views.PostList.as_view())
]
