from tarfile import ENCODING
import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.google.com"
DEPTH=2

crawled_website =set()

def crawler(url,depth):
    if depth<DEPTH and a_tag not in crawled_website:
        try:
            
            html = requests.get(url)
        except requests.exceptions.ConnectionError:
            return
        if html.status_code==200:
            html.encoding=ENCODING

        soup = BeautifulSoup(html.text,"html.parser")
        print(soup.prettify())


    for a_tag in soup.find_all("a"):
         print(a_tag.get("href"))
