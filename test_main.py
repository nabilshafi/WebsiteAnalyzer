import unittest
from main import *

class TestMain(unittest.TestCase):


    def test_url_status(self):
        self.assertTrue(url_status("https://pypi.org/project/build/"))
        self.assertFalse(url_status("youtube.com"))
        self.assertFalse(url_status("youtube"))
        self.assertFalse(url_status("https://www.youtubeeeee.com"))
        self.assertFalse(url_status("#"))

    def test_internal_links(self):
        url = "http://olympus.realpython.org/profiles"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        gather_links(url, soup)
        self.assertEqual(len(internal_links),3)

