from steamScrape import sScrape
while True:
    print('Program which displays information of games after a search by the game name\n'
        + '(Type \'40sec\' to exit)\nWhen entering game name, enter words within the official game name for better accuracy')
    print('')
    input('')
    gameName = 'hollow knight'
    if gameName in '40sec':
        break
    else:
        sGameList = sScrape(gameName)
        max_ = 0
        for i in sGameList:
            if len(i.name) > max_:
                max_ = len(i.name)
        max_ += 80
        for i in sGameList:
            i.display_all(max_)