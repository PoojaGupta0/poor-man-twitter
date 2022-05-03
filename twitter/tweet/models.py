from django.db import models
from django.utils.timezone import now


class Tweet(models.Model):
    user_name = models.CharField(max_length=250, verbose_name="Username")
    message = models.TextField(max_length=50, verbose_name="Tweet")
    created_at = models.CharField(
        max_length=50,
        default=now().strftime("%m/%d/%Y, %H:%M:%S"),
        verbose_name="Tweet Date"
    )

    def __str__(self):
        return self.user_name
