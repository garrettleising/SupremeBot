from os import walk
from os import path

profiles = []
keyList = ["itemName", "size", "itemColor", "itemType", "name", "email", "telephone", "address", "aptUnitEtc", "zipcode", "city", "state", "country", "creditCardNumber", "experationMonth", "experationYear", "cvv"]

def readFile(toRead):
    orderedProfile = {}
    splice = toRead.split('"')
    i = 1
    for key in keyList:
        orderedProfile[key] = splice[i]
        i+=2
    return orderedProfile

def readProfile():
    for root, dirs, files in walk(".\Profiles"):
        #dirs is any folders
        for name in files:
            f = open(path.join(root,name), "r")
            toRead = ''.join(f.readlines())
            profiles.append(readFile(toRead))

def addProfile():
    print("Not done yet!")

def removeProfile():
    print("Not done yet!")

def run():
    for instance in profiles:
        print(instance)
        #open
        #load supreme
        #refreshen
        #clicky
        #clicky clicky filly profiley
        #if failed go back baby

readProfile()
#make some gui to go between add, read, delete, and run.