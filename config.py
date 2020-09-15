import os

class Config:
  SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&apiKey={}'
  TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apikey={}'
  EVERYTHING_URL = 'https://newsapi.org/v2/everything?q=trending&language=en&apiKey={}'
  BUSINESS_URL = 'https://newsapi.org/v2/top-headlines?category=business&apiKey={}'
  SPORTS_URL = 'https://newsapi.org/v2/top-headlines?category=sports&apiKey={}'
  NEW_API_KEY = os.environ.get('NEW_API_KEY')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}