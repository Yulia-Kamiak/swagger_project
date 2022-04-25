import pytest
from random import randint
import randomaizer

@pytest.fixture()
def user_data():
    random_data = randomaizer.RandomData()
    random_name = random_data.generate_word(6)
    data = [{
            "id": 0,
            "username": random_name,
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
          }]
    return data

@pytest.fixture()
def get_login():
    data = [{
            "username": "string",
            "password": "string"
          }]
    return data

@pytest.fixture()
def create_user():
    random_data = randomaizer.RandomData()
    random_name = random_data.generate_word(6)
    data = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
          }
    return data

@pytest.fixture()
def store_inventory():
    data = {
          "sold": randint(1, 10),
          "string": randint(1, 100),
          "pending": randint(1, 100),
          "available": randint(1, 1000)
        }
    return data

@pytest.fixture()
def store_oder():
    data = {
          "id": 0,
          "petId": 0,
          "quantity": 0,
          "shipDate": "2021-09-04T10:14:03.177Z",
          "status": "placed",
          "complete": True
        }
    return data

@pytest.fixture()
def pet_to_store():
    pet = {
          "id": 0,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "doggie",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
    return pet
