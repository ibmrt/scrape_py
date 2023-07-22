class SteamGame:
    def __init__(id, sName, sLink, sPrice, sSetupList):
        id.name = sName
        id.link = sLink
        id.price = sPrice
        id.setupList = sSetupList
    def display_all(id, max):
        distance = len(id.name) + 7
        t_distance = max - (distance + len('Requirements:'))
        print(id.name + '        Requirements:' + id.price.rjust(t_distance, ' '))
        for i in id.setupList:
            print(''.ljust(distance, ' '), i)
        print(''.ljust(max, '-'))