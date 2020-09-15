import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
  """
  Test case for the sources class
  """

  def setUp(self):
    """
    Set up method that will run before every class
    """

    self.new_source = Sources('abc_news','ABC News','Good news all day')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))

  def test_init(self):
    """
    test to see if the object is correctly instantiated
    """
    self.assertEqual(self.new_source.id, 'abc_news')
    self.assertEqual(self.new_source.name, 'ABC News')
    self.assertEqual(self.new_source.description, 'Good news all day')

