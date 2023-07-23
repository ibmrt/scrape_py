class SteamGame:
    def __init__(id, sName, sLink, sPrice, sSetupList):
        id.name = sName
        id.link = sLink
        id.price = sPrice
        id.setupList = sSetupList
    def display_all(id, max):
        distance = len(id.name) + 8
        t_distance = max - (distance + len('Requirements:'))
        print(id.name + '        Requirements:' + id.price.rjust(t_distance, ' '))
        for i in id.setupList:
            print(''.ljust(distance, ' '), i)
        print(''.ljust(max, '-'))

class GogGame:
    def __init__(idg, gName, gLink, gPrice, gSetupList):
        idg.name = gName
        idg.link = gLink
        idg.price = gPrice
        idg.setupList = gSetupList
    def check_replace(idg, id):
        if idg.name.__eq__(id.name):
            idg.setupList = id.setupList
    def display_all_g(idg, max):
        distance = len(idg.name) + 8
        t_distance = max - (distance + len('Requirements:'))
        print(idg.name + '        Requirements:' + idg.price.rjust(t_distance, ' '))
        for i in idg.setupList:
            print(''.ljust(distance, ' '), i)
        print(''.ljust(max, '-'))