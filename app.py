from flask import Flask, render_template
from lib import user_repository
from lib.database_connection import DatabaseConnection
from lib.user import User


app = Flask(__name__)
#this is for the session cookies
app.secret_key = "app_config_key"


@app.route('/', methods=['POST'])
def get_index():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
    
