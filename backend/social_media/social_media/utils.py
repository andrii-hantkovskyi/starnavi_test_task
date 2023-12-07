import datetime

from django.conf import settings


def get_parsed_date(date):
    return datetime.datetime.strptime(date, settings.DATE_FORMAT)
