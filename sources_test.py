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

    self.new_source = Sources('ABC News','Good news all day','http://www.abc.net.au/news','general','en','au')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
  unittest.main()