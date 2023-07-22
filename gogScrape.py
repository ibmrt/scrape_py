from bs4 import BeautifulSoup
import urllib.request

#def gogScape(name):
name = "dread templar"
gNameList = name.split(" ")
name = name.replace(" ","%20")
website = urllib.request.urlopen("https://www.gog.com/en/games?query=" + name).read()
soup = BeautifulSoup(website, "html.praser")