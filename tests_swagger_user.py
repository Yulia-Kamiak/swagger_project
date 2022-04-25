import requests
import api_urls
from conftest import user_data
from headers import HEADERS
from json import dumps

#  pytest -s -vv tests_swagger_user.py

def test_user_post_createWithList(user_data):
    '''Creates list of users with given input array'''
    user = requests.post(url=api_urls.User.USER, headers=HEADERS, data=dumps(user_data))
    # print("\n\t", user.text)
    assert user.status_code == 200, 'Falling'

def test_user_get_username(get_login, user_data):
    """Given: created user"""
    username = user_data[0]["username"]
    requests.post(url=api_urls.User.USER, headers=HEADERS, data=dumps(user_data))
    print("\n\t", username)
    """When: Call find user by name"""
    user = requests.get(url=api_urls.User.USERNAME + username)
    "Then: user should be found"
    assert user.status_code == 200, 'Falling'

def test_user_put_username(user_data, create_user):
    """Given: created user"""
    username = user_data[0]["username"]
    requests.post(url=api_urls.User.USER, headers=HEADERS, data=dumps(user_data))
    """Update user"""
    user_update = requests.put(url=api_urls.User.USERNAME + username, headers=HEADERS, data=dumps(create_user))
    assert user_update.status_code == 200, 'Falling'


def test_user_del_username(user_data, create_user):
    """Given: created user"""
    username = user_data[0]["username"]
    requests.post(url=api_urls.User.USER, headers=HEADERS, data=dumps(user_data))
    """Delete user"""
    user_delete = requests.delete(url=api_urls.User.USERNAME + username, headers=HEADERS, data=dumps(create_user))
    assert user_delete.status_code == 200, 'Falling'

def test_user_login(get_login):
    """Logs user into the system"""
    user_loin = requests.get(url=api_urls.User.USERLOGIN, headers=HEADERS, data=dumps(get_login))
    assert user_loin.status_code == 200, 'Falling'

def test_user_logout(get_login):
    """logs out current logged in the session"""
    user_loin = requests.get(url=api_urls.User.USERLOGOUT)
    assert user_loin.status_code == 200, 'Falling'

def test_list_users(user_data):
    """Creates list of users with given input array"""
    users_list = requests.post(url=api_urls.User.USERS_LIST, headers=HEADERS, data=dumps(user_data))
    assert users_list.status_code == 200, 'Falling'

def test_create_user(create_user):
    """This can only be done by the logged in user"""
    create_user = requests.post(url=api_urls.User.CREATE_USER, headers=HEADERS, data=dumps(create_user))
    assert create_user.status_code == 200, 'Falling'




