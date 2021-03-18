import os, psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_marshmallow import Marshmallow
from flask_cors import CORS

cache_config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

if app.config['ENV']=='development':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig')

db = SQLAlchemy(app)
Migrate(app,db)
ma = Marshmallow(app)
app.config.from_mapping(cache_config)
cache = Cache(app)
cors = CORS(app)

#import blueprints
from pauperapi.core.views import core
from pauperapi.content.views import content
from pauperapi.boxes.views import boxes
from pauperapi.cards.views import cards
from pauperapi.decks.views import decks



#register blueprints to the app
app.register_blueprint(core)
app.register_blueprint(content)
app.register_blueprint(cards)
app.register_blueprint(boxes)
app.register_blueprint(decks)

