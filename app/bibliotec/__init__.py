import os

from flask import Flask
from flask_restful import Api
from .main.routes import main
from .api.routes import apis
from .errors.handler import errors
from .api.handler import BooksInquiry


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(apis)

api = Api(app)
api.add_resource(BooksInquiry, "/books/v1/volumes")
