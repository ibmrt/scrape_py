from bs4 import BeautifulSoup
import urllib.request
import gameObj

#def sScrape (name):

linkList = []
nameList = []
priceList = []
reqList = []

name = input(':\n')
keywords = name.split(' ')
name = name.replace(' ', '+')

search_site = urllib.request.urlopen('https://store.steampowered.com/search/?term=' + name).read()
search_soup = BeautifulSoup(search_site, 'html.parser')

for item in search_soup.find_all(attrs = {'data-gpnav' : 'item'}):
    hLink = item.get('href')
    checker = True
    for i in keywords:
        if hLink != None:
            if i.lower() not in hLink.lower():
                checker = False
        else:
            checker = False
    if checker:
        linkList.append(hLink)
        for child in item.children:
            try:
                nameList.append(child.find('span', class_='title').contents[0])
            except:
                pass
        for child in item.children:
            try:
                priceSec = child.find('div', class_='col search_discount_and_price responsive_secondrow')
                if priceSec != None:
                    if len(priceSec.contents) > 1:
                        priceList.append(child.find('div', class_='discount_final_price').contents[0])
                    else:
                        priceList.append('Unavailable or Free')
            except:
                pass
for link in linkList:
    gamePage = urllib.request.urlopen(link).read()
    pageSource = BeautifulSoup(gamePage, 'html.parser')
    reqSec = pageSource.find('div', class_='game_area_sys_req sysreq_content active')
    print('1')
    try:
        if len(reqSec) > 1:
            print(type(reqSec.contents))
            pass
        else:
            print('None')
    except:
        pass