from faker import Faker
from random import randint
import pytest
import os
from client import ApiClient
from dotenv import load_dotenv
from user_dc import User

load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

fake_eng = Faker("en_US")

username = f'test_{fake_eng.first_name()}_{randint(1, 20)}'
password = fake_eng.bothify(text='?????##?##?##', letters='ABCDE!@#$%^&zxc')


@pytest.fixture
def user_data(client_acc):
    user = User(userName=USER_NAME, password=PASSWORD)
    return user.__dict__


@pytest.fixture
def client_acc():
    return ApiClient(url='https://demoqa.com/Account/v1')


@pytest.fixture
def auth_client_acc(client_acc, user_data):
    # client_acc.post('/Authorized', json=dict(userName=user_creds.userName, password=user_creds.password))
    client_acc.post('/Authorized', json=user_data)
    return client_acc
    # yield
    # client_acc.delete(f'/User/{uuid}')


@pytest.fixture
def user_random_payload():
    user = User(userName=username, password=password)
    return user.__dict__
