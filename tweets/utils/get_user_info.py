from django.db.models import Q

from ..models import Tweet
from users.models import User


def get_user_latest_tweet(user_id, contacted_user_id, tweet_type):
    return (
        Tweet.objects.filter(
            Q(
                Q(reply_to_user_id=contacted_user_id)
                | Q(retweet_to_user_id=contacted_user_id),
                user_id=user_id,
            )
            | Q(
                Q(reply_to_user_id=user_id) | Q(retweet_to_user_id=user_id),
                user_id=contacted_user_id,
            ),
            tweet_type=tweet_type,
        )
        .order_by("-created_at")
        .first()
    )


def get_user_info(user_id, contacted_user_id, tweet_type):
    user = User.objects.filter(user_id=user_id).first()
    latest_tweet = get_user_latest_tweet(user_id, contacted_user_id, tweet_type)

    return {
        "user_id": user.user_id,
        "screen_name": user.screen_name,
        "description": user.description,
        "contact_tweet_text": latest_tweet.text if latest_tweet else None,
    }
