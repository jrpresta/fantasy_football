from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


# create an application instance to handle requests
application = Flask(__name__)
application.config.from_object(Config)


bootstrap = Bootstrap(application)


# from app import classes
# from app import routes
from app import main
