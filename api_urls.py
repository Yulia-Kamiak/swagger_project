from random import randint

BASE_URL = "https://petstore.swagger.io/v2"

class User():
    """Urls in user`s group"""
    USER = BASE_URL + "/user/createWithList"
    USERNAME = BASE_URL + "/user/"
    USERLOGIN = BASE_URL + "/user/login"
    USERLOGOUT = BASE_URL + "/user/logout"
    USERS_LIST = BASE_URL + "/user/createWithArray"
    CREATE_USER = BASE_URL + "/user"

class Store():
    """Urls in group in store"""
    STORE_INVENTORY = BASE_URL + "/store/inventory"
    STORE_ODER = BASE_URL + "/store/order"
    ODER_ID = BASE_URL + f"/store/order/{randint(1, 10)}"

class Pet():
    """Urls in group in pet"""
    PET_TO_STORE = BASE_URL + "/pet"
    FIND_PET_BY_STATUS = BASE_URL + "/pet/findByStatus"
    FIND_PET_BY_ID = BASE_URL + f"/pet/{4}"
    FIND_PET_BY_FORM = BASE_URL + f"/pet/{4}"
    UPLOADS_AN_IMAGE = BASE_URL + f"/pet/{2}/uploadImage"

