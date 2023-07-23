from steamScrape import sScrape
from gogScrape import gScrape
from gameObj import SteamGame
from gameObj import GogGame

def separator(max):
    print(''.ljust(max, '-'))

print('Program which displays information of games after a search by the game name\n'
+ '(Type \'40sec\' to exit)\nWhen entering game name, enter words within the official game name for better accuracy')
while True:
    gameName = input('Enter game name here (avoid using special characters, use space to separate keywords)\n(ex: counter Strike, hollow knight, Only up, TERRARIA):\n')
    if gameName in '40sec':
        break
    else:
        print('One Moment...')
        sGameList = sScrape(gameName)
        gGameList = gScrape(gameName)
        lenS = len(sGameList)
        lenG = len(gGameList)

        max_ = 0
        for i in sGameList:
            if len(i.name) > max_:
                max_ = len(i.name)
        max_ += 80
        for i in range(len(gGameList)):
            for item in sGameList:
                gGameList[i].check_replace(item)
        separator(max_)
        print('Most compatible results:')
        if lenG != 0 and lenG != 0:
            gGame = GogGame('n', 'l', 'p', ['s'])
            for i in gGameList:
                if sGameList[0].name.__eq__(i.name):
                    gGame = i
            separator(max_)
            print('Steam:')
            separator(max_)
            sGameList[0].display_all(max_)
            print('Gog:')
            separator(max_)
            gGame.display_all_g(max_)
        elif lenG == 0 and lenS == 0:
            separator(max_)
            print('Steam:')
            separator(max_)
            print('None')
            separator(max_)
            print('Gog:')
            separator(max_)
            print('None')
            separator(max_)
        elif lenG == 0:
            separator(max_)
            print('Steam:')
            separator(max_)
            sGameList[0].display_all(max_)
            print('Gog:')
            separator(max_)
            print('None')
            separator(max_)
        else:
            separator(max_)
            print('Steam:')
            separator(max_)
            print('None')
            separator(max_)
            print('Gog:')
            separator(max_)
            gGameList[0].display_all_g(max_)

        separator(max_)
        print('Steam')
        separator(max_)
        if lenG != 0:
            for i in sGameList:
                i.display_all(max_)
        else:
            print('None found by the keyword: ' + gameName)
            separator(max_)
        print('Gog')
        separator(max_)
        if lenG != 0:
            for i in gGameList:
                i.display_all_g(max_)
        else:
            print('None found by the keyword: ' + gameName)
            separator(max_)
        
    input('Press to continue...')