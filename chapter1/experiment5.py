from urllib.request import urlopen
from bs4 import BeautifulSoup
from re

pages = set()
def getLinks(pageURL):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageURL)
    bsObj = BeautifulSoup(html, "html.parser")
    links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^/wiki/")):
    for link in links:
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage)
            
getLinks("")
