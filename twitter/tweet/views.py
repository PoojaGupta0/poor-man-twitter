from rest_framework.generics import ListCreateAPIView
from .models import Tweet
from .serilaizers import TweetSerializer


class ListCreateTweet(ListCreateAPIView):
    """

    """
    queryset = Tweet.objects.all().order_by('created_at')
    serializer_class = TweetSerializer
