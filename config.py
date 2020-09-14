import os

class Config:
  SOURCE_BASE_URL='https://newsapi.org/v2/sources?apiKey={}'
  TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?apiKey={}'
  NEW_API_KEY = os.environ.get('NEW_API_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}