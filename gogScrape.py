from bs4 import BeautifulSoup
import urllib.request
from gameObj import GogGame

def gScrape(name):
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
        if pageSource.find("div", class_ = "product-actions-price") !=None:
            for i in pageSource.find_all("div", class_ = "product-actions-price"  ):
                priceList.append("$"+i.contents[1].contents[0])
        else:
            priceList.append('Unavaliable or Free')
        reqList.append(['None or Unavailable'])
    for i in range(len(nameList)):
        sGameList.append(GogGame(nameList[i], linkList[i], priceList[i], reqList[i]))
    
    return sGameList