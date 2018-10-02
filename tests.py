import unittest
from utils import get_excuse, get_hashtag


class UtilsTestCase(unittest.TestCase):

    @staticmethod
    def test_returns_an_excuse():
        assert isinstance(get_excuse(), str)

    @staticmethod
    def test_returns_an_hashtag():
        assert isinstance(get_hashtag(), str)

    @staticmethod
    def test_length_twitt():
        assert len(get_excuse()) <= 140


if __name__ == '__main__':
    unittest.main()
