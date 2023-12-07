import datetime

import pytz
from django.conf import settings
from django.contrib.auth import get_user_model

from users.services.common import get_user_by_id

User = get_user_model()


def update_last_user_request(user_id: int) -> None:
    user = get_user_by_id(user_id)
    user.last_request = datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))
    user.save()

