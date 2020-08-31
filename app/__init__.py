from flask import Flask
from jinja2 import Environment
from hamlish_jinja import HamlishExtension, HamlishTagExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask.ext.heroku import Heroku


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'abc' # TODO change in prod

db = SQLAlchemy(app)
migrate = Migrate(app, db)

env = Environment(extensions=[HamlishExtension])
env.hamlish_file_extensions=('.haml', '.html.haml')
env.hamlish_enable_div_shortcut=True
env.hamlish_mode='debug'
app.jinja_env.add_extension(HamlishTagExtension)
app.jinja_env.add_extension(HamlishExtension)


from app import views, models


