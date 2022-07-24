import math
from django.db.models import Count, Q

from ..models import Hashtag


def get_current_user_hashtags(user_id):
    return list(
        Hashtag.objects.filter(user_id=user_id)
        .values("hashtag_name")
        .annotate(count=Count("hashtag_name"))
    )


def get_other_users_hashtags(user_id, current_user_hashtags):
    return list(
        Hashtag.objects.filter(
            ~Q(user_id=user_id), hashtag_name__in=current_user_hashtags
        )
        .values("user_id", "hashtag_name")
        .annotate(count=Count("hashtag_name"))
        .order_by("user_id")
    )


def get_hashtag_score(same_tag_count):
    new_dict = {}

    for tag in same_tag_count:
        new_dict[tag] = (
            1 + math.log(1 + same_tag_count[tag] - 10)
            if same_tag_count[tag] > 10
            else 1
        )

    return new_dict


def calculate_hashtag_score(user_id):
    current_user_hashtags = get_current_user_hashtags(user_id)
    current_user_hashtag_names = [x["hashtag_name"] for x in current_user_hashtags]
    other_users_hashtags = get_other_users_hashtags(user_id, current_user_hashtag_names)

    same_tag_count = {}

    for user_hashtag in other_users_hashtags:
        x = None
        for current_user_hashtag in current_user_hashtags:
            if current_user_hashtag["hashtag_name"] == user_hashtag["hashtag_name"]:
                x = current_user_hashtag
                break

        if x:
            user_hashtag["count"] = user_hashtag["count"] + x["count"]

        if user_hashtag["user_id"] in same_tag_count:
            same_tag_count[user_hashtag["user_id"]] = (
                same_tag_count[user_hashtag["user_id"]] + user_hashtag["count"]
            )
        else:
            same_tag_count[user_hashtag["user_id"]] = user_hashtag["count"]

    return get_hashtag_score(same_tag_count)
