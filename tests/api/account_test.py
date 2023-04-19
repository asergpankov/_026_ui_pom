import pytest
import requests
import os
from client import ApiClient
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


def test_create_new_user(client_acc, user_random_payload):
    status, body = client_acc.post('/User', json=user_random_payload)
    print(user_random_payload)
    print(status)
    print(body)
# {'userName': 'test_Caleb_10', 'password': '$ADDx91c91z52'}
# {'userID': '1e6467af-c50e-420b-a7d7-caddcb8ab372', 'username': 'test_Caleb_10', 'books': []}
# todo need to validate userId like uuid

def test_user_already_exist(client_acc, user_data):
    status, body = client_acc.post('/User', json=user_data)
    assert status == 406
    assert body['message'] == 'User exists!'


def test_auth_user(auth_client_acc):
    # status, body = auth_client_acc.post('/Authorized', json=dict(userName=auth_client_acc.userName, password=auth_client_acc.password))
    print(auth_client_acc)
    # assert status == 200
    # assert body == True, f'body has not contains True. Only {body}'
    uuid = '1e6467af-c50e-420b-a7d7-caddcb8ab372'
    print(auth_client_acc.get(f'/User/{uuid}'))


def test_logout_user(auth_client_acc):
    pass


def test_generate_token_for_auth_user(auth_client_acc, user_data):
    status, body = auth_client_acc.post('/GenerateToken', json=user_data)
    print(status, body)
    # assert status == 200
    # assert len(body['token']) >= 50  # todo need to validate token
    # assert body['result'] == 'User authorized successfully.'


def test_get_user_on_uuid(client_acc, auth_client_acc):
    uuid = 'd68cf060-a17d-4aed-8783-abf71b61a569'
    status, body = auth_client_acc.get(f'/User/{uuid}')
    print(status)
    print(body)
    # assert status == 200


def test_delete_user_on_uuid(client_acc):
    uuid = '1e6467af-c50e-420b-a7d7-caddcb8ab372'
    status, body = client_acc.delete(f'/User/{uuid}')
    print(status)
    print(body)
    # assert status == 200
