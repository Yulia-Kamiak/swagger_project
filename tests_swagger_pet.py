import pytest
import requests
import api_urls
from headers import HEADERS
from json import dumps

#  pytest -s -vv tests_swagger_pet.py

def test_new_pet(pet_to_store):
    '''Add new pet to the store'''
    pet_to_store = requests.post(url=api_urls.Pet.PET_TO_STORE, headers=HEADERS, data=dumps(pet_to_store))
    assert pet_to_store.status_code == 200, 'Falling'

def test_update_pet(pet_to_store):
    '''Update an existing pet'''
    pet_update = requests.put(url=api_urls.Pet.PET_TO_STORE, headers=HEADERS, data=dumps(pet_to_store))
    assert pet_update.status_code == 200, 'Falling'

def test_find_pet():
    '''Finds pet by status'''
    find_pet = requests.get(url=api_urls.Pet.FIND_PET_BY_STATUS)
    assert find_pet.status_code == 200, 'Falling'

@pytest.mark.xfail
def test_find_pet_by_id():
    '''Finds pet by status'''
    find_pet_by_id = requests.get(url=api_urls.Pet.FIND_PET_BY_ID)
    # print("\n\t", find_pet_by_id.url)
    assert find_pet_by_id.status_code == 200, 'Falling'

@pytest.mark.skip(reason="There is a random value")
def test_update_pet_by_form():
    '''Updates a pet in the store with form data'''
    update_pet = requests.post(url=api_urls.Pet.FIND_PET_BY_FORM)
    # print("\n\t", update_pet.url)
    assert update_pet.status_code == 200, 'Falling'

@pytest.mark.xfail
def test_delete_pet(pet_to_store):
    '''Deletes a pet'''
    delete_pet = requests.delete(url=api_urls.Pet.FIND_PET_BY_ID)
    # print("\n\t", delete_pet.url)
    assert delete_pet.status_code == 200, 'Falling'

def test_uploads_image():
    '''Uploads an image'''
    with open('./Robot_Framework/data/f2637562392edd24809a100a0211e6f8-symbols-design-logo-icon-design.jpg', 'rb') as f:
        files = {"file": f}
        image = requests.post(url=api_urls.Pet.UPLOADS_AN_IMAGE, files=files)
    assert image.status_code == 200, 'Falling'



