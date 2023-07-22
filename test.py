from bs4 import BeautifulSoup
import urllib.request

name = "read or not"
gNameList = name.split(" ")
name = name.replace(" ","+")
website = urllib.request.urlopen("https://gg.deals/games/?title=" + name).read()
soup = BeautifulSoup(website, "html.parser")
linkList = []

for section in soup.find_all("a", class_ = "full-link"):
    link = section.get("href")
    print(link)
    checker = True
    for i in gNameList:
        if i.lower() not in link.lower():
            checker = False
    if checker:
        linkList.append(link)
            