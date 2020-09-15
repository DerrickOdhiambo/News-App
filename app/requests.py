import urllib.request, json
from .models import Sources,TopHeadlines,Everything

api_key = None

base_url = None

everything_base_url = None

top_headlines_base_url = None

def configure_request(app):
  global api_key,base_url,top_headlines_base_url,everything_base_url
  api_key = app.config['NEW_API_KEY']
  base_url = app.config['SOURCE_BASE_URL']
  top_headlines_base_url = app.config['TOP_HEADLINES_URL']
  everything_base_url = app.config['EVERYTHING_URL']

def get_new():
  """
  Function that gets json response to our url request
  """

  get_source_url = base_url.format(api_key)

  with urllib.request.urlopen(get_source_url) as url:
    get_sources_data = url.read()
    get_source_response = json.loads(get_sources_data)

    source_results = None

    if get_source_response['sources']:
      sources_results_list = get_source_response['sources']
      source_results = process_results(sources_results_list)

  return source_results


def process_results(source_list):
  source_results = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')


    source_object = Sources(id, name, description)
    source_results.append(source_object)

  return source_results


def get_source_details(id):
  get_source_details_url = top_headlines_base_url.format(id,api_key)

  with urllib.request.urlopen(get_source_details_url) as url :
    source_details_data = url.read()
    source_details_response = json.loads(source_details_data)

    article_results = None

    if source_details_response['articles']:
      source_details_list = source_details_response['articles']
      article_results = process_source_data(source_details_list)

  return article_results



def process_source_data(top_headlines_list):
  top_results = []
  for item in top_headlines_list:

    author = item.get('author')
    title = item.get('title')
    url = item.get('url')
    image_path = item.get('urlToImage')
    publishedAt = item.get('publishedAt')
    content = item.get('content')

    articles_objects = TopHeadlines(author, title, url, image_path, publishedAt, content)
    top_results.append(articles_objects)

  return top_results



def get_everything() :
  '''
  gets the request for the everything endpoint
  '''
  get_everything_url = everything_base_url.format(api_key)

  with urllib.request.urlopen(get_everything_url) as url :
    get_everything_data = url.read()
    get_everything_response = json.loads(get_everything_data)

    everything_results =  None 

    if get_everything_response['articles'] :
      everything_results_list = get_everything_response['articles']
      everything_results = process_everything_results(everything_results_list)

  return everything_results 

def process_everything_results(everything_results_list) :
  '''
  processes the json object into a list.
  '''
  everything_results = []
  for everything_item in everything_results_list :

    author = everything_item.get('author')
    title = everything_item.get('title')
    url = everything_item.get('url')
    urlToImage = everything_item.get('urlToImage')
    publishedAt = everything_item.get('publishedAt')
    content = everything_item.get('content')

    everything_object = Everything(author, title, url, urlToImage, publishedAt, content)
    everything_results.append(everything_object)

  return everything_results