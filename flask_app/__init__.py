from flask import Flask

from env import key

app = Flask(__name__)

app.secret_key = key