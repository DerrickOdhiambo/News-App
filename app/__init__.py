from flask import Flask
from flask_fontawesome import FontAwesome
from config import config_options

fa = FontAwesome()

def create_app(config_name):

  app = Flask(__name__)

  #initializing fontawesome
  fa.init_app(app)

  # creating the app configurations
  app.config.from_object(config_options[config_name])


  # registering a blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #settign config
  from .requests import configure_request
  configure_request(app)

  return app


