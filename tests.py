import unittest
from utils import get_excuse, get_hashtag


class UtilsTestCase(unittest.TestCase):

    def test_returns_an_excuse(self):
        assert isinstance(get_excuse(), str)

    def test_returns_an_hashtag(self):
        assert isinstance(get_hashtag(), str)

    def test_length_twitt(self):
        resp = get_excuse()
        self.assertTrue(len(resp) <= 140, 'INFO: Normal length of Twitter message')
        self.assertFalse(len(resp) > 140, 'ERROR: Length of Twitter message is too long')


if __name__ == '__main__':
    unittest.main()
