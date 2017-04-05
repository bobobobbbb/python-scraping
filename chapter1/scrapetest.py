#国外的网址前要加proxychains4
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return "raise a HTTPError"
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return "sraise a AttributeError"
    return title

print("Input the url: ")
url = input()
title = getTitle(url)
if title == None:
    print(title)
print(title)