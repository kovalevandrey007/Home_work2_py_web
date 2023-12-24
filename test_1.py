import pytest
import yaml
from module import Site
import time


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

    site = Site(testdata['address'])


def test_step1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    assert err_label.text == '401'


def test_step2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    true_label = site.find_element('xpath', select_hello_user)
    # print(site.get_element_property('xpath', select_hello_user, 'Name'))
    # print('*'*50)
    # print(true_label.text)
    # print('*' * 50)
    # assert True
    assert true_label.text == f'Hello, {testdata["login"]}'

def test_step3(site, select_input_login, select_input_password, select_input_button, add_post_button, add_title, add_discription, add_content, save_button):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn1 = site.find_element('css', select_input_button)
    btn1.click()
    time.sleep(3)
    btn2 = site.find_element('css', add_post_button)
    btn2.click()
    input3 = site.find_element('xpath', add_title)
    input3.send_keys(testdata['title'])
    input4 = site.find_element('xpath', add_discription)
    input4.send_keys(testdata['description'])
    input5 = site.find_element('xpath', add_content)
    input5.send_keys(testdata['content'])
    btn3 = site.find_element('css', save_button)
    btn3.click()
    assert True

def test_step4(site, select_input_login, select_input_password, select_input_button, get_posts):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    find_text = site.find_element('xpath', get_posts)
    assert find_text.text == f'{testdata["title"]}'




