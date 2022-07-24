import math
from django.db.models import Count

from utils.helpers import convert_list_to_dict, sum_dict
from ..models import Tweet


def get_reply_count_from_me(user_id):
    return list(
        (
            Tweet.objects.filter(user_id=user_id, tweet_type="reply")
            .values("reply_to_user_id")
            .annotate(count=Count("reply_to_user_id"))
        )
    )


def get_reply_count_from_others(user_id):
    return list(
        (
            Tweet.objects.filter(reply_to_user_id=user_id, tweet_type="reply")
            .values("user_id")
            .annotate(count=Count("user_id"))
        )
    )


def get_retweet_count_from_me(user_id):
    return list(
        (
            Tweet.objects.filter(user_id=user_id, tweet_type="retweet")
            .values("retweet_to_user_id")
            .annotate(count=Count("retweet_to_user_id"))
        )
    )


def get_retweet_count_from_others(user_id):
    return list(
        (
            Tweet.objects.filter(retweet_to_user_id=user_id, tweet_type="retweet")
            .values("user_id")
            .annotate(count=Count("user_id"))
        )
    )


def get_interaction_score(reply_count, retweet_count):
    new_dict = {}
    keys = list(reply_count.keys()) + list(retweet_count.keys())

    for key in keys:
        val1 = reply_count.get(key) if reply_count.get(key) else 0
        val2 = retweet_count.get(key) if retweet_count.get(key) else 0

        new_dict[key] = math.log(1 + 2 * val1 + val2)

    return new_dict


def calculate_interaction_score(user_id):

    reply_count_from_me = convert_list_to_dict(get_reply_count_from_me(user_id))
    reply_count_from_others = convert_list_to_dict(get_reply_count_from_others(user_id))
    retweet_count_from_me = convert_list_to_dict(get_retweet_count_from_me(user_id))
    retweet_count_from_others = convert_list_to_dict(
        get_retweet_count_from_others(user_id)
    )
    reply_count = sum_dict(reply_count_from_me, reply_count_from_others)
    retweet_count = sum_dict(retweet_count_from_me, retweet_count_from_others)

    return get_interaction_score(reply_count, retweet_count)
