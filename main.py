import re, sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen
import validators
from bs4 import BeautifulSoup

internal_links = set()
external_links = set()
all_links = set()

# Checking the url status
def url_status(url):
    if validators.url(url): # Validating the url format
        try:
            if urlopen(url).getcode() == 200:
                return True
        except HTTPError:
            return False
        except URLError:
            return False
    return False

# Gathering all links inside webpage and dividing accordingly
def gather_links(url, soup):
    host = urlparse(url).hostname
    if host.startswith('www.'):
        host = host[4:]
    if host.endswith("/"):
        host = host[:-1]
    pattern = re.compile("^(/)")  # For relative links
    for link in soup.find_all("a", href=True):
        if re.findall(pattern, link['href']):  #Finding relative links
            new_url = url + link['href']
            internal_links.add(new_url)
        elif host not in link['href'] and validators.url(link['href']): #Finding the external links
            external_links.add(link['href'])
        else:
            internal_links.add(link['href'])
        all_links.add(link['href'])




# Verifying that links are reachabl
def reachable_links():
    reach = 0
    for link in external_links:
        if url_status(link):
            reach += 1
    return reach

#Checking the URL version
def check_version(soup):
    if "<!DOCTYPE" in str(soup):
        partitioned_string = str(soup).split('>')[0]
        if "HTML 4" in partitioned_string:
            print("Website using HTML 4")
        elif "XHTML" in partitioned_string:
            print("Website using XTML")
        else:
            print("Website using HTML 5")
        return 1
    return 0

if __name__ == '__main__':

    url = sys.argv[1]
    if url_status(url):
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        gather_links(url, soup)
        reach = reachable_links()
        forms = soup.find('form')

        # Print statements
        if not check_version(soup):
            print("Version not found")
        print("Tittle: " + soup.title.string)
        print("No. of distinct links: " + str(len(all_links)))
        print("No. of external links: " + str(len(external_links)))
        print("No. of external reachable links: " + str(reach))
        if 'login' in str(forms).lower():
            print("Login form exists")
    else:
        print("Invalid URL")

