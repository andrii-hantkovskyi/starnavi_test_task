from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils.timezone import make_aware

from posts.models import PostLike
from social_media.utils import get_parsed_date


def get_date_ranged_likes(date_from: str, date_to: str) -> list[PostLike]:
    parsed_date_from, parsed_date_to = get_parsed_date(date_from), get_parsed_date(date_to)
    parsed_date_from, parsed_date_to = make_aware(parsed_date_from), make_aware(parsed_date_to)

    return (
        PostLike.objects.filter(
            created_at__range=[parsed_date_from, parsed_date_to]
        ).values(date=TruncDate('created_at')).annotate(count=Count('id'))
    )
