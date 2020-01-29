from flask import Flask
from flask_sqlalchamy import SQLAlchamy

db = SQLAlchamy()

app = Flask(__name__)
db.init_app(app)

