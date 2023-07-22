from bs4 import BeautifulSoup
import urllib.request

#def gogScape(name):
name = "dread templar"
gNameList = name.split(" ")
name = name.replace(" ","%20")
website = urllib.request.urlopen("https://www.gog.com/en/games?query=" + name).read()
<<<<<<< HEAD
soup = BeautifulSoup(website, "html.parser")
print(website)

for section in soup.find_all("a", class_='product-tile product-tile--grid'):
    link = section.get("href")
    checker = True
    for i in gNameList:
        if i.lower() not in link.lower():
            checker = False

=======
soup = BeautifulSoup(website, "html.praser")
priceList = []
>>>>>>> 92fc30333212ae204720e7b4ee9d9d16f603ff77
