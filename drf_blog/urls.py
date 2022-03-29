from django.urls import include, path
from rest_framework import routers, include
from drf_blog import views


urlpatterns = [
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<1nt:pk>/vote', views.VoteCreate.as_view()),
    path('api-auth/', include('rest_framework.urls'))    
]

