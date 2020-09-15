class Sources:
  """
  Sources from different places 
  """
  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description


class Articles:
  """
  Source articles from different sources
  """

  def __init__(self, author, title, url, urlToImage,publishedAt, content):
    self.author = author
    self.title = title
    self.url = url
    self.image_path = urlToImage
    self.publishedAt = publishedAt
    self.content = content


class Everything:
  """
  Source articles from different sources that shows different kinds of articles
  """

  def __init__(self, author, title, url, urlToImage, publishedAt, content):
    self.author = author
    self.title = title
    self.url = url
    self.image_path = urlToImage
    self.publishedAt = publishedAt
    self.content = content

class Sports:
  """
  Source articles for sports
  """

  def __init__(self, author, title, url, urlToImage,publishedAt, content):
    self.author = author
    self.title = title
    self.url = url
    self.image_path = urlToImage
    self.publishedAt = publishedAt
    self.content = content


class Business:
  """
  Source articles for business stories
  """

  def __init__(self, author, title, url, urlToImage,publishedAt, content):
    self.author = author
    self.title = title
    self.url = url
    self.image_path = urlToImage
    self.publishedAt = publishedAt
    self.content = content

