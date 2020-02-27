from django.utils.crypto import get_random_string
from cut_app import models


def cut():
    short_url = get_random_string(length=7)
    check_if_exist = models.Links.objects.filter(short_url=short_url)
    if not check_if_exist:
        return short_url
    else:
        cut()


