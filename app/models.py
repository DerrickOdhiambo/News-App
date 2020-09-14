class Sources:
  """
  Sources from different places 
  """
  def __init__(self, id, name, description, url, category, language, country):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country


class TopHeadlines:
  """
  Source articles from different sources
  """

  def __init__(self, author, title, description, url, urlToImage,publishedAt, content):
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.image_path = urlToImage
    self.publishedAt = publishedAt
    self.content = content

