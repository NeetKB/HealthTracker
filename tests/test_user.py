from lib.user import *

"""
User constructs with a fullname, email and password
"""
def test_user_constructs():
    user = User(1, "Avnita Bhandal", "ab@example.com", "Password£123")
    assert user.id == 1
    assert user.fullname == "Avnita Bhandal"
    assert user.email == "ab@example.com"
    assert user.password == "Password£123"


"""
We can format user to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Avnita Bhandal", "ab@example.com", "Password£123")
    assert str(user) == "User(1, Avnita Bhandal, ab@example.com, Password£123)"


"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Avnita Bhandal", "ab@example.com", "Password£123")
    user2 = User(1, "Avnita Bhandal", "ab@example.com", "Password£123")
    assert user1 == user2