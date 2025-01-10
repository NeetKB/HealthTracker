from flask import Flask, render_template
from lib.user_repository import *
from lib.database_connection import DatabaseConnection
from lib.user import User
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
import os

app = Flask(__name__)
#this is for the session cookies
app.secret_key = "app_config_key"


@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('/homepage.html')

@app.route('/', methods=["POST"])
def register_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    fullname = request.form["fullname"]
    email = request.form["email"]
    password = request.form["password"]

    user = User(None, fullname, email, password)

    try:
        repository.create_user(user)
        print("User created successfully") 
        return render_template("/register_success")
    
    except Exception as e:
        print(f"Error during registration: {e}")  # Log error
        error = str(e)
        return render_template("homepage.html", error=error)



@app.route('/register_success', methods=['GET'])
def register_successful():
    return render_template('register_success.html')


if __name__ == '__main__':

    print(f"App environment: {os.getenv('APP_ENV')}")
    print(f"App testing config: {app.config['TESTING']}")
    app.run(debug=True)
    
