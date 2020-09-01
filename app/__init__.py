from flask import Flask
from jinja2 import Environment
from hamlish_jinja import HamlishExtension, HamlishTagExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask.ext.heroku import Heroku

# Load flask app from config.py
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'Wdj5ccVm4pGbDy' # TODO change in prod

# Setup db
db = SQLAlchemy(app)

# Setup db migrations
migrate = Migrate(app, db)

# Setup HAML
# See hamlish-jinja https://github.com/Pitmairen/hamlish-jinja
env = Environment(extensions=[HamlishExtension])
env.hamlish_file_extensions=('.haml', '.html.haml')
env.hamlish_enable_div_shortcut=True
env.hamlish_mode='debug'
app.jinja_env.add_extension(HamlishTagExtension)
app.jinja_env.add_extension(HamlishExtension)


from app import views, models


