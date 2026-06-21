import pytest
import uuid
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()

def test_getuser_validation(apis):
    response=apis.get('users')
    print(response.json())
    assert response.status_code==200
    assert len(response.json())>0

def test_create_user(apis,load_user_data):
    new_data=load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    new_data["email"] = unique_email
    response=apis.post('users',new_data)
    print(response.json())
    assert response.status_code==201

    assert response.json()["name"]==new_data["name"]

    assert response.json()["email"]==unique_email


def test_update_user(apis,load_user_data):
    updated_data = load_user_data["updated_user"]
    response = apis.put('users/1', updated_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"]==updated_data["name"]

    assert response.json()["email"]==updated_data["email"]

def test_delete_user(apis):
    response=apis.delete('users/1')
    print(response.json())


