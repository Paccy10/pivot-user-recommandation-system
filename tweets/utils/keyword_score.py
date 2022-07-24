import math
from django.db.models import Q

from utils.helpers import count_occurrences
from ..models import Tweet


def get_user_tweets(user_id, tweet_type):
    tweets = []

    if tweet_type == "reply":
        tweets = Tweet.objects.filter(
            Q(user_id=user_id) | Q(reply_to_user_id=user_id), tweet_type=tweet_type
        )

    if tweet_type == "retweet":
        tweets = Tweet.objects.filter(
            Q(user_id=user_id) | Q(retweet_to_user_id=user_id), tweet_type=tweet_type
        )

    if tweet_type == "both":
        tweets = Tweet.objects.filter(
            Q(user_id=user_id)
            | Q(reply_to_user_id=user_id)
            | Q(retweet_to_user_id=user_id),
            Q(tweet_type="reply") | Q(tweet_type="retweet"),
        )

    return list(tweets)


def get_key_on_reply(tweet, user_id):
    return user_id if tweet.user_id == user_id else tweet.reply_to_user_id


def get_key_on_retweet(tweet, user_id):
    return user_id if tweet.user_id == user_id else tweet.retweet_to_user_id


def get_key(tweet, tweet_type, user_id):
    key = None

    if tweet_type == "reply":
        key = get_key_on_reply(tweet, user_id)

    elif tweet_type == "retweet":
        key = get_key_on_retweet(tweet, user_id)

    else:
        key = (
            get_key_on_reply(tweet, user_id)
            if tweet.reply_to_user_id
            else get_key_on_retweet(tweet, user_id)
        )

    return key


def get_keyword_score(total_matches):
    new_dict = {}

    for key in total_matches:
        new_dict[key] = 1 + math.log(total_matches[key] + 1)

    return new_dict


def calculate_keyword_score(user_id, tweet_type, phrase, hashtag):
    tweets = get_user_tweets(user_id, tweet_type)
    total_matches = {}

    for tweet in tweets:
        key = get_key(tweet, tweet_type, user_id)

        if phrase in tweet.text:
            total_matches[key] = total_matches.get(key, 0) + count_occurrences(
                tweet.text, phrase
            )

        hashtags = tweet.hashtags.split(",") if tweet.hashtags else []

        for tag in hashtags:
            if hashtag.lower() == tag.lower():
                total_matches[key] = total_matches.get(key, 0) + 1

    return get_keyword_score(total_matches)
