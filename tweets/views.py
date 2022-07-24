from rest_framework.response import Response
from rest_framework.decorators import api_view
from tweets.utils.get_user_info import get_user_info
from tweets.utils.hashtag_score import calculate_hashtag_score

from tweets.utils.interaction_score import calculate_interaction_score
from tweets.utils.keyword_score import calculate_keyword_score
from utils.helpers import multiply_dict


@api_view(["GET"])
def q2(request):
    user_id = request.GET.get("user_id")
    hashtag = request.GET.get("hashtag")
    phrase = request.GET.get("phrase")
    tweet_type = request.GET.get("type")

    interaction_score = calculate_interaction_score(user_id)
    hashtag_score = calculate_hashtag_score(user_id)
    keyword_score = calculate_keyword_score(user_id, tweet_type, phrase, hashtag)

    ranking_score = multiply_dict(interaction_score, hashtag_score, keyword_score)
    data = []

    for key in ranking_score:
        user_info = get_user_info(key, user_id, tweet_type)
        tweet_data = {**user_info, "ranking_score": ranking_score[key]}
        data.append(tweet_data)

    data = sorted(data, key=lambda d: d["ranking_score"], reverse=True)

    return Response(data)
