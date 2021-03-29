import unittest
from web_analyzer import *

class TestMain(unittest.TestCase):


    def test_url_status(self):
        self.assertTrue(url_status("https://www.youtube.com"))
        self.assertTrue(url_status("http://youtube.com"))
        self.assertFalse(url_status("youtube"))
        self.assertFalse(url_status("https://www.youtubeeeee.com"))
        self.assertFalse(url_status("#"))

    def test_internal_links(self):
        url = "http://olympus.realpython.org/profiles"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        internal_links, external_links, all_links = gather_links(url, soup)
        self.assertEqual(len(internal_links),3)
        self.assertEqual(len(external_links),0)

