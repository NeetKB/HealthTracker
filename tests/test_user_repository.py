from lib.database_connection import DatabaseConnection
from lib.user_repository import *
from lib.user import *
import pytest
from app import get_flask_database_connection, app


"""
User is created 
"""
def test_user_can_create_account(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repo = UserRepository(db_connection)
    repo.create_user(User(None, "Tina Newman", "tn@example.com", "Passwords123!"))
    res =  repo.get_user_details("tn@example.com") 
    assert res == User(3,"Tina Newman", "tn@example.com", pass_hash("Passwords123!") )


"""test when we call user repository we can read their details"""
def test_read_user_details(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    user = repository.get_user_details("sam@example.com")
    assert user == User(1, "Sam", "sam@example.com", "a109e36947ad56de1dca1cc49f0ef8ac9ad9a7b1aa0df41fb3c4cb73c1ff01ea")

"""
User must have a valid email address
"""
def test_invalid_email_creates_exception(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.create_user(User(None, "John Doe", "samexample.com", "password123!"))
    error_msg = str(err.value)
    assert error_msg == "This email is invalid."
"""
User must have unique email address else exception raised
"""
def test_account_creation_duplicate_email(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.create_user(User(None, "Sam English", "sam@example.com", "password123!"))
    error_msg = str(err.value)
    assert error_msg == "This email is already in use."

"""
User must have valid password: 8 characters in length 
"""
def test_password_valid_length_fail(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.create_user(User(None, "Jane Doe", "jane@example.com", "prd2"))
    error_msg = str(err.value)
    assert error_msg == "This password does not comply with requirements! Must have at least 8 characters."

"""
User must have valid password:  must have special characters
"""

def test_create_password_special_character_fail(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        repository.create_user(User(None, "Jack", "jackemail@email.com", "password1"))
    error_msg = str(err.value)
    assert error_msg == "This password does not comply with requirements! Must have at least one special character."
"""
Must be able to delete account
"""
def test_user_details_deletion(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    repository.delete_account("Sam")
    account = repository.get_user_details("sam@example.com")
    assert account == None

"""test that password can be updated correctly"""
def test_update_password_success(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    user = repository.update_password("sam@example.com", "qwertyuiop!")
    updated_profile = repository.get_user_details("sam@example.com")
    assert updated_profile == User(1, "Sam", "sam@example.com", pass_hash("qwertyuiop!"))

"""test that password can be updated incorrectly (special characters)"""
def test_update_password_fail_special(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        user = repository.update_password("sam@example.com", "qwertyuiop")
    error_msg = str(err.value)
    assert error_msg == "This password does not comply with requirements! Must have at least one special character."
    

"""test that password can be updated incorrectly (character count)"""
def test_update_password_fail_number(db_connection):
    db_connection.seed("seeds/health_tracker.sql")
    repository = UserRepository(db_connection)
    with pytest.raises(Exception) as err:
        user = repository.update_password("sam@example.com", "we")
    error_msg = str(err.value)
    assert error_msg == "This password does not comply with requirements! Must have at least 8 characters."