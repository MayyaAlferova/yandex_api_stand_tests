from copy import copy

import requests
from requests import Response

import configuration
from data import HEADER_DATA


def get_url(path: str) -> str:
    return f'{configuration.URL_SERVICE}{path}'


def post_new_user(user_data: dict) -> Response:
    return requests.post(
        url=get_url(configuration.PATH_CREATE_USER),
        headers=HEADER_DATA,
        json=user_data,
    )


def post_new_client_kits(auth_token: str, kit_body: dict) -> Response:
    headers = copy(HEADER_DATA)
    headers.update({"Authorization": f"Bearer {auth_token}"})
    return requests.post(
        url=get_url(configuration.PATH_CREATE_KIT),
        headers=headers,
        json=kit_body
    )
