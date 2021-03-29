import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_url_status(self):
        self.assertTrue(url_status("https://www.youtube.com"))
        self.assertFalse(url_status("youtube.com"))
        self.assertFalse(url_status("youtube"))
        self.assertFalse(url_status("https://www.youtubeeeee.com"))
        self.assertFalse(url_status("#"))


