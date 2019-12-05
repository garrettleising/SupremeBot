import threading
from SupremeBot import doIt
from os import walk
from os import path

#keyList is the order for profile.txt files
profiles = []
keyList = ["itemName", "size", "itemColor", "itemType", "name", "email", "telephone", "address", "aptUnitEtc", "zipcode", "city", "state", "country", "creditCardNumber", "experationMonth", "experationYear", "cvv"]

#readFile decomposes each .txt file into a dictionary using keyList
def readFile(toRead):
    orderedProfile = {}
    splice = toRead.split('"')
    i = 1
    for key in keyList:
        #check if splice[i] exists. if not returns nothing instead of OrderedProfile.
        orderedProfile[key] = splice[i]
        i+=2
    return orderedProfile

#readProfile will fetch all in the .\Profiles folder.
def readProfile():
    for root, dirs, files in walk(".\Profiles"):
        #dirs is any folders
        for name in files:
            f = open(path.join(root,name), "r")
            toRead = ''.join(f.readlines())
            profiles.append(readFile(toRead))

#addProfile will add a profile to the .\Profiles folder
def addProfile():
    print("Not done yet!")

def removeProfile():
    print("Not done yet!")

#Strictly for debugging
def printProfile():
    for instance in profiles:
        print(instance)

#Temp holder for running SupremeBot.py
def run():
    for instance in profiles:
        task = threading.Thread(target = doIt, args = (instance,))
        task.start()

#Temp holder for running run() (should be done with gui clicks)
readProfile()
run()
