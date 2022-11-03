import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from geoip2 import errors

YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'


def yelp_search(keyword='Pizzaria', location='São Paulo'):
    headers = {"Authorization": f"Bearer {settings.YELP_API_KEY}"}

    params = {"term": keyword, "location": location}

    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)
    # if not r.ok:
    #     return {"status": r.status_code, "reason": r.reason, "text": r.text}
    return r.json()


def get_client_data():
    geoip = GeoIP2()
    ip = get_random_ip()

    try:
        return geoip.city(ip)
    except errors.AddressNotFoundError:
        return None


def get_random_ip():
    return '.'.join([str(randint(0, 255)) for _ in range(4)])
