from os import walk
from os import path

## ideas: make a list for the ordered dict so it can index in a parallel array.

keyList = ["itemName", "size", "itemColor", "itemType", "name", "email", "telephone", "address", "aptUnitEtc", "zipcode", "city", "state", "country", "creditCardNumber", "experationMonth", "experationYear", "cvv"]
profiles = []

def readFile(toRead):
    orderedProfile = {}
    splice = toRead.split('"')
    i = 1
    for key in keyList:
        orderedProfile[key] = splice[i]
        i+=2
    return orderedProfile

for root, dirs, files in walk(".\Profiles"):
    #dirs is any folders
    for name in files:
        f = open(path.join(root,name), "r")
        toRead = ''.join(f.readlines())
        profiles.append(readFile(toRead))

for instance in profiles:
    print(instance)
    #open
    #load supreme
    #refreshen
    #clicky
    #clicky clicky filly profiley
    #if failed go back baby