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
        if i not in hLink:
            checker = False
    if checker:
        linkList.append(hLink)
        