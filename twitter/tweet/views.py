from rest_framework.generics import ListCreateAPIView
from .models import Tweet
from .serilaizers import TweetSerializer


class ListCreateTweet(ListCreateAPIView):
    """
    ListCreateTweet:
        A view set to do create and read operation,
        method:- GET, POST
    """
    queryset = Tweet.objects.all().order_by('-created_at', 'user_name')
    serializer_class = TweetSerializer
