import re
from urllib.parse import parse_qsl
from urllib.parse import urlparse
from urllib.parse import urlunparse


def append_to_query_string(url, key, value) -> str:
    """Append a parameter to the url querystring
    """
    url = list(urlparse(url))
    query = dict(parse_qsl(url[4]))
    query[key] = value
    url[4] = '&'.join(f'{p}={v}' for p, v in query.items())

    return urlunparse(url)


def snake_case(string: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


def snakesify_dict_keys(dict_for_snakesifing: dict) -> dict:
    return {snake_case(key): dict_for_snakesifing[key] for key in dict_for_snakesifing.keys()}


__all__ = [
    snake_case,
]
