from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLink(articleURL):
    html = urlopen("http://en.wikipedia.org" + articleURL)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLink("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = link[random.randint(0, links.size() - 1)]
    print(newArticle)
    links = getLink(newArticle)
