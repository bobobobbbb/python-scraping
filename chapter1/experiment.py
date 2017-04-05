from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text)
nameList2 = bsObj.findAll(text="the prince")
nameList3 = bsObj.findAll("", {"class":"green"})
nameList4 = bsObj.findAll("", )
print(len(nameList2))
