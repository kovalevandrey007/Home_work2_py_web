import pytest
import yaml
from module import Site
import requests
import json

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def select_input_login():
    return '''//*[@id="login"]/div[1]/label/input'''

@pytest.fixture()
def select_input_password():
    return '''//*[@id="login"]/div[2]/label/input'''

@pytest.fixture()
def select_input_button():
    return '''button'''

@pytest.fixture()
def select_error():
    return '''//*[@id="app"]/main/div/div/div[2]/h2'''

@pytest.fixture()
def select_hello_user():
    return '''//*[@id="app"]/main/nav/ul/li[3]/a'''

@pytest.fixture()
def site():
    site_class = Site(testdata['address'])
    yield site_class
    site_class.close()

@pytest.fixture()
def add_post_button():
    return '''button'''

@pytest.fixture()
def add_title():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label'''

@pytest.fixture()
def add_discription():
    return '''//*[@id="create-item"]/div/div/div[2]/div/label'''


@pytest.fixture()
def add_content():
    return '''//*[@id="create-item"]/div/div/div[3]/div/label'''

@pytest.fixture()
def save_button():
    return '''button'''

@pytest.fixture()
def get_posts():
    return '''//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'''
