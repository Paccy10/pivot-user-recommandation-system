from django.db import models

from django.db import models


class Tweet(models.Model):

    tweet_id = models.BigIntegerField(unique=True, null=False)
    text = models.TextField(null=False)
    user_id = models.BigIntegerField(null=False)
    user_screen_name = models.CharField(max_length=200, null=False)
    user_description = models.CharField(max_length=250, null=True)
    tweet_type = models.CharField(max_length=100, null=True)
    reply_to_tweet_id = models.BigIntegerField(null=True)
    reply_to_user_id = models.BigIntegerField(null=True)
    retweet_to_tweet_id = models.BigIntegerField(null=True)
    reply_to_user_id = models.BigIntegerField(null=True)
    retweet_to_user_id = models.BigIntegerField(null=True)
    hashtags = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(null=False)

    class Meta:
        db_table = "tweets"


class Hashtag(models.Model):
    tweet_id = models.BigIntegerField(null=False)
    user_id = models.BigIntegerField(null=False)
    hashtag_name = models.CharField(max_length=250, null=False)

    class Meta:
        db_table = "hashtags"
        unique_together = ("tweet_id", "user_id", "hashtag_name")
