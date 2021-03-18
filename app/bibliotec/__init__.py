from flask import Flask
from .main.routes import main
from .errors.handler import errors


app = Flask(__name__)
app.config['SECRET_KEY'] = '5ece3cf37c407bee4d3ceca1'
app.register_blueprint(main)
app.register_blueprint(errors)
