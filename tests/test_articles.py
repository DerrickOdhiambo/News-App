import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
  """
  Test case for the sources class
  """

  def setUp(self):
    """
    Set up method that will run before every class
    """

    self.new_source = Articles('John Terry','ABC News','https://www.abc.com','https://image.com','April 12 2001','Good work')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Articles))

  def test_init(self):
    """
    test to see if the object is correctly instantiated
    """
    self.assertEqual(self.new_source.author, 'John Terry')
    self.assertEqual(self.new_source.title, 'ABC News')
    self.assertEqual(self.new_source.url, 'https://www.abc.com')
    self.assertEqual(self.new_source.image_path, 'https://image.com')
    self.assertEqual(self.new_source.publishedAt, 'April 12 2001')
    self.assertEqual(self.new_source.content, 'Good work')

