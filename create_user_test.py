# эта функция меняет значения в параметре firstName
from sender_stat_request import post_new_user, get_users_table


def get_user_body(first_name) -> dict:
    return {'firstName': first_name, 'phone': '+79995553322', 'address': 'г. Москва, ул. Пушкина, д. 10'}


def test_create_user_2_letter_in_first_name_get_success_response() -> None:
    resp = post_new_user(get_user_body('AAA'))
    print(resp.status_code, resp.json())

    assert resp.status_code == 201
    assert resp.json()['authToken']

    resp = get_users_table()
    print(resp.text)
