import requests
from requests import Response

import configuration


def get_url(path: str) -> str:
    return f'{configuration.URL_SERVICE}{path}'


def get_docs() -> Response:
    return requests.get(f'{configuration.URL_SERVICE}{configuration.DOC_PATH}')


def get_logs() -> Response:
    return requests.get(f'{configuration.URL_SERVICE}{configuration.LOG_MAIN_PATH}', params={'count': 20})


def get_users_table() -> Response:
    return requests.get(get_url(path=configuration.USERS_TABLE_PATH))


def post_new_user(user_data: dict) -> Response:
    return requests.post(
        url=get_url(configuration.CREATE_USER_PATH),
        headers={'Content-Type': 'application/json'},
        json=user_data,
    )


def post_products_kits() ->Response:
    return requests.post(
        url=get_url(path=configuration.PRODUCTS_KITS_PATH),
        headers={'Content-Type': 'application/json'},
        json={'ids': [1, 2, 3]}
    )
#
#
# response = post_products_kits()
#
# print(f'Response [{response.status_code}]: {response.headers}\n{response.json()}')
