from django.urls import path

from .views import LikeViewApi, FollowingViewApi

urlpatterns = [
    path('like/', LikeViewApi.as_view()),
    path('following/', FollowingViewApi.as_view())
]