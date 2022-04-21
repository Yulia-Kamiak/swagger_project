import pytest
import requests
import api_urls
from headers import HEADERS
from json import dumps

#  pytest -s -vv tests_swagger_store.py

def test_store_inventory(store_inventory):
    '''Returns pet inventories by status'''
    store = requests.get(url=api_urls.Store.STORE_INVENTORY, headers=HEADERS, data=dumps(store_inventory))
    assert store.status_code == 200, 'Falling'

def test_store_oder(store_oder):
    '''Place an oder for a pet'''
    store_oder = requests.post(url=api_urls.Store.STORE_ODER, headers=HEADERS, data=dumps(store_oder))
    assert store_oder.status_code == 200, 'Falling'

@pytest.mark.skip(reason="there is a random value")
def test_store_oder_id():
    '''Place an oder for a pet'''
    oder_id = requests.get(url=api_urls.Store.ODER_ID, headers=HEADERS)
    # print("\n\t", oder_id.url)
    assert oder_id.status_code == 200, 'Falling'

@pytest.mark.xfail
def test_store_oder_delete():
    '''Delete an oder for a pet'''
    oder_delete = requests.delete(url=api_urls.Store.ODER_ID, headers=HEADERS)
    # print("\n\t", oder_delete.url)
    assert oder_delete.status_code == 200, 'Falling'