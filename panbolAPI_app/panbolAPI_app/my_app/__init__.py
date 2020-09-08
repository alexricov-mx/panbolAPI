from flask import Flask

app = Flask(__name__)

#rest
from my_app.rest_api.panbol_api import panbol_view