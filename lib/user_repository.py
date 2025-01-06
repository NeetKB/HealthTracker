from lib.user import *
import re
import hashlib



def pass_hash(password):
    binary_password = password.encode("utf-8")
    return hashlib.sha256(binary_password).hexdigest()

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    

    def create_user(self, user):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        row = self._connection.execute('select * from users where fullname = %s', [user.fullname])
        if row == []:
            if (re.fullmatch(regex, user.email)):
                row = self._connection.execute('select * from users where email = %s', [user.email])
                if row == []:
                    if len(user.password) >= 8:            
                        if any(elem in '!@$%&' for elem in user.password) == True:
                            self._connection.execute('insert into users (fullname, email, password) values (%s, %s, %s)', [user.fullname, user.email, pass_hash(user.password)])
                        else:
                            raise Exception("This password does not comply with requirements! Must have at least one special character.")
                    else:
                        raise Exception("This password does not comply with requirements! Must have at least 8 characters.")
                else:
                    raise Exception("This email is already in use.")
            else:
                raise Exception("This email is invalid.")
        else:
            raise Exception("This fullname has been taken!")
        
    def get_user_details(self, fullname):
        rows = self._connection.execute('select * from users where fullname = %s', [fullname])
        if rows == []:
            return None
        else:
            row = rows[0]
            return User(row["id"], row["fullname"], row["email"], row["password"])
        
    def delete_account(self, fullname):
        self._connection.execute('delete from users where fullname = %s', [fullname])

    def update_password(self, fullname, new_password):
        row = self._connection.execute('select * from users where fullname = %s', [fullname])
        if row != []:
            if len(new_password) >= 8:            
                if any(elem in '!@$%&' for elem in new_password) == True:
                    self._connection.execute('update users set password = %s where fullname = %s', [pass_hash(new_password), fullname])
                else:
                    raise Exception("This password does not comply with requirements! Must have at least one special character.")
            else:
                raise Exception("This password does not comply with requirements! Must have at least 8 characters.")
        else:
            raise Exception("User not found.")
        
        