from bs4 import BeautifulSoup
import urllib.request

#def gogScape(name):
name = "dread templar"
gNameList = name.split(" ")
name = name.replace(" ","%20")
website = urllib.request.urlopen("https://www.gog.com/en/games?query=" + name).read()
soup = BeautifulSoup(website, "html.parser")
sGameList = []
linkList = []
nameList = []
priceList = []
reqList = []


for section in soup.find_all("a", class_='product-tile product-tile--grid'):
    link = section.get("href")
    checker = True
    for i in gNameList:
        if i.lower() not in link.lower():
            checker = False
    if checker:
        linkList.append(link)

for link in linkList:
    gamePage = urllib.request.urlopen(link).read()
    pageSource = BeautifulSoup(gamePage, "html.parser")
    nameList.append(pageSource.find('h1', class_='productcard-basics__title').contents[0].strip())
    for i in pageSource.find_all("div", class_ = "product-actions-price"  ):
        priceList.append("$"+i.contents[1].contents[0])
    print(pageSource.find_all(attrs = {'ng-bind-html' : 'requirement.minimum'}))