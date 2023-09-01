from typing import Optional

from requests import Response

from data import USER_DATA
from sender_stat_request import post_new_user, post_new_client_kits


def get_access_token(response: Response) -> Optional[str]:
    return response.json().get('authToken')


def positive_assert(response: Response, name: str) -> None:
    assert response.status_code == 201
    assert response.json()['name'] == name


def negative_assert(response: Response) -> None:
    assert response.status_code == 400


def test_create_kit__allowed_length_1() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'а'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__allowed_length_511() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__not_allowed_empty_name() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': ''}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    negative_assert(response=response)


def test_create_kit__not_allowed_length_512() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    negative_assert(response=response)


def test_create_kit__allowed_english_name() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'QWErty'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__allowed_russian_name() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'Мария'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__allowed_special_symbols() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': '"№%@",'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__allowed_spaces() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 'Человек и КО'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__allowed_numbers() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': '123'}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    positive_assert(response=response, name=kit_body['name'])


def test_create_kit__not_allowed_missed_name() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    negative_assert(response=response)


def test_create_kit__not_allowed_wrong_name_type() -> None:
    response: Response = post_new_user(user_data=USER_DATA)
    auth_token = get_access_token(response=response)
    kit_body = {'name': 123}

    response: Response = post_new_client_kits(auth_token=auth_token, kit_body=kit_body)

    negative_assert(response=response)
