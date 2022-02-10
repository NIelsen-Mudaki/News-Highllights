from flask import Flask
from flask import Blueprint
main = Blueprint('main',__name__)
from config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from . import views,errors