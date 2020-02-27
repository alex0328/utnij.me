from django.utils.crypto import get_random_string

def cut():
    short_url = get_random_string(length=7)
    return short_url


