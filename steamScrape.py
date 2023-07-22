from bs4 import BeautifulSoup
import urllib.request
import gameObj
from gameObj import SteamGame

def sScrape (name):
    sGameList = []
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
        try:
            if len(reqSec.contents) > 1:
                singleReqList = []
                try:
                    len(reqSec.find('li').contents) > 0
                    for reqInfo in reqSec.find_all('li'):
                        try:
                            singleReqList.append(reqInfo.contents[0].contents[0])
                        except:
                            pass
                        try:
                            singleReqList.append(reqInfo.contents[1])
                        except:
                            pass
                except:
                    for reqInfo in reqSec.find_all('p'):
                        try:
                            singleReqList.append(reqInfo.contents[0].contents[0])
                        except:
                            pass
                        try:
                            reqInfoList = reqInfo.contents[1].split(', ')
                            for i in reqInfoList:
                                singleReqList.append(i)
                        except:
                            pass
        except:
            reqList.append(['None'])
    try:
        for i in range(len(nameList)):
            sGameList.append(SteamGame(nameList[i], linkList[i], priceList[i], reqList[i]))
        return sGameList
    except:
        print('Error')