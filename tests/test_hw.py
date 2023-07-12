import pytest
from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password

pf = PetFriends()

def test_get_api_key_for_invalid_user(email = invalid_email, password = invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403 or status == 400
    print('\nОшибка, неверный ввод данных пользователя, статус - ', status)

def test_post_new_pets_without_photo(name = 'sanya', age = '68', animal_type = 'proger'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert len(result) > 0

def test_post_new_pets_without_name( name = '', age = '1', animal_type = 'neponyatno'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 403 or status == 400

def test_post_new_pets_without_animal_type ( name = 'pivozavr', age = '1', animal_type = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 403 or status == 400

def test_post_new_pets_without_age ( name = 'pivozavr', age = '', animal_type = 'dog'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_without_photo(auth_key, name, animal_type, age)
    assert status == 403 or status == 400

def test_post_new_pets_with_photo_inalid_format(name = 'Alex', age = '8', animal_type = 'Кот', pet_photo = "files/romb.pdf"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_api_pets_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status != 200

def test_get_list_of_pets_with_invalid_api_key (auth_key = '12345', filter = ' '):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 500

def test_update_pets_none_info (name = "", age = "", animal_type = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, age, animal_type)

    assert status != 200



