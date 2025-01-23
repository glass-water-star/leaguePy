from os import path
import json
# import pytest
from leaguepy.models.registrations import Registration, Registrations
from leaguepy.models.members import Member, Members

# @pytest.fixture
# def new_registration():
#     return RegistrationModel(username="testuser", email="testuser@example.com", password="password123")

def test_registration_get():
    folder_path = path.abspath(path.dirname(__file__))
    folder = path.join(folder_path, "test_data")
    json_file = path.join(folder, 'registrations_response.json')
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    model = Registrations.validate_python(json_data)
    assert len(model) > 1

def test_members_get():
    folder_path = path.abspath(path.dirname(__file__))
    folder = path.join(folder_path, "test_data")
    json_file = path.join(folder, 'members_response.json')
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    model = Members.validate_python(json_data)
    assert len(model) > 1
    
def test_member_get():
    folder_path = path.abspath(path.dirname(__file__))
    folder = path.join(folder_path, "test_data")
    json_file = path.join(folder, 'member_response.json')
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    model = Member(**json_data)
    assert model.firstName == "Jane"
    assert model.lastName == "Finch"
    