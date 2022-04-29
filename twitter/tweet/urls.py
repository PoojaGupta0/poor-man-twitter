from django.urls import path
from .views import ListCreateTweet


urlpatterns = [
    path('add_tweet/', ListCreateTweet.as_view(), name="create-tweet"),
]
