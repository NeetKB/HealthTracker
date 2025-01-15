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

### HOMEPAGE/REGISTRATION ROUTES ###

@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('/homepage.html')

@app.route('/', methods=["POST"])
def register_user():
    connection = get_flask_database_connection(app)
    print("Connected to database!")
    repository = UserRepository(connection)

    fullname = request.form["fullname"]
    email = request.form["email"]
    password = request.form["password"]

    user = User(None, fullname, email, password)

    try:
        repository.create_user(user)
        print("User created successfully") 
        return redirect("/register_success")
    
    except Exception as e:
        print(f"Error during registration: {e}")  # Log error
        error = str(e)
        return render_template("homepage.html", error=error)


### LOGIN ROUTES ###
@app.route('/login', methods=['GET'])
def get_login():
    just_registered = request.args.get('registered') == 'true'
    return render_template('login.html', just_registered=just_registered)

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    return render_template('/dashboard.html')

@app.route('/login', methods=['POST'])
def log_in_user():
    connection = get_flask_database_connection(app)
    print("Connected to database!")
    repo = UserRepository(connection)

    email = request.form["email"]
    password = request.form["password"]

    if repo.check_password(email, password) == True:
        user = repo.get_user_details(email)
        # Set the user ID in session
       
        session['user_id'] = user.id
        session['email'] = user.email
        print("User logged in")
        return redirect("/dashboard")
    else:
        errors = "Incorrect email or password"
        return render_template("login.html", errors=errors)



if __name__ == '__main__':

    print(f"App environment: {os.getenv('APP_ENV')}")
    print(f"App testing config: {app.config['TESTING']}")
    app.run(debug=True)
    
