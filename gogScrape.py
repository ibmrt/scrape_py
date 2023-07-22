from bs4 import BeautifulSoup
import urllib.request

#def gogScape(name):
name = "dread templar"
gNameList = name.split(" ")
name = name.replace(" ","%20")
website = urllib.request.urlopen("https://www.gog.com/en/games?query=" + name).read()
soup = BeautifulSoup(website, "html.parser")
print(website)

for section in soup.find_all("a", class_='product-tile product-tile--grid'):
    link = section.get("href")
    checker = True
    for i in gNameList:
        if i.lower() not in link.lower():
            checker = False

