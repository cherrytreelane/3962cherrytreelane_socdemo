#!/usr/bin/env python3

import os.path
from pathlib import Path

def getMilk():
    print("Milk")

def getDrano():
    print("Drano")

def getEggs():
    print("Eggs")

def getClorox():
    print("Clorox")

def getVegetables():
    print("Vegetables")

def getRaid():
    print("Raid")

def getButter():
    print("Butter")

def getLysol():
    print("Lysol")

def cleanTop():
    print("You cleaned the top of the fridge using " + getClorox())

def cleanShelves():
    print("You cleaned the shelves of the fridge using " + getLysol())

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getMilk()
    getDrano()
    getEggs()
    getClorox()
    getVegetables()
    getRaid()
    getButter()
    getLysol()
    print("Now let's clean the fridge!")
    cleanTop()
    cleanShelves()


if __name__ == "__main__":
    main()
