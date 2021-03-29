# This is a sample Python script.
import re
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import validators
from bs4 import BeautifulSoup

internal_links = set()
external_links = set()
all_links = set()


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def url_status(url):

    if validators.url(url):
        try:
            if urlopen(url).getcode() == 200:
                return True
        except HTTPError:
            return False
        except URLError:
            return False
    return False

def gather_links(url, soup):

    domain_name = url.split(".")[1] + "." + url.split(".")[2]
    pattern = re.compile("^(/)")  # For relative links
    for link in soup.find_all("a", href=True):
        if re.findall(pattern, link['href']):  # Finding relative links
            new_url = url + link['href']
            internal_links.add(new_url)
        elif domain_name not in link['href'] and validators.url(link['href']):
            external_links.add(link['href'])
        else:
            internal_links.add(link['href'])
        all_links.add(link['href'])

def reachable_links():

    reach = 0
    for link in external_links:
        if url_status(link):
            reach += 1
    return reach

if __name__ == '__main__':

    url = "https://www.oreilly.com/"
    if url_status(url):
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        gather_links(url, soup)
        reach = reachable_links()

        print("Tittle: " + soup.title.string)
        print("No. of distinct links: " + str(len(all_links)))
        print("No. of external links: " + str(len(external_links)))
        print("No. of external reachable links: " + str(reach))

        print(external_links)

    else:
        print("Invalid URL")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
