from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Tweet


class TestTweet(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.tweet = Tweet.objects.create(
            user_name="test_user",
            message="This is test tweet for test case"
        )
        Tweet.objects.create(
            user_name="test_user1",
            message="This is test tweet for test case"
        )

    def test_create_tweet(self):
        url = reverse('create-tweet')
        payload = {
            "user_name": "jhon",
            "message": "This is test tweet for test case"
        }
        response = self.client.post(
            url,
            data=payload
        )
        assert response.status_code == status.HTTP_201_CREATED

        # testing with invalid data (message length greater 60)
        payload['message'] = "This is test tweet for test case This is test tweet for test case This is test tweet for " \
                             "test caseThis is test tweet for test caseThis is test tweet for test caseThis is test " \
                             "tweet for test case "
        response = self.client.post(
            url,
            data=payload
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # testing with invalid data
        payload.pop('user_name')
        response = self.client.post(
            url,
            data=payload
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_list_tweet(self):
        url = reverse('create-tweet')
        response = self.client.get(
            url,
        )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0].get('user_name') == self.tweet.user_name
