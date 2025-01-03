from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
#this is for the session cookies
app.config = os.getenv("app_config_key")

@app.route('/', methods=['POST'])
def get_index():
    return render_template('homepage.html')