from flask import Flask
from flask_restful import Api
from flask import Flask

app = Flask(__name__, template_folder='templates')
api = Api(app)
secret_key_tg = ""

app.json.ensure_ascii = False

