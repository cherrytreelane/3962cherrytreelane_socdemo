#!/usr/bin/env python3

import os.path
from pathlib import Path

def getMilk():
    return "Milk"

def getDrano():
    return "Drano"

def getEggs():
    return "Eggs"

def getClorox():
    return "Clorox"

def getVegetables():
    return "Vegetables"

def getRaid():
    return "Raid"

def getButter():
    return "Butter"

def getLysol():
    return "Lysol"

def cleanTop():
    print("You cleaned the top of the fridge using " + getClorox())

def cleanShelves():
    print("You cleaned the shelves of the fridge using " + getLysol())

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    print(getMilk())
    print(getDrano())
    print(getEggs())
    print(getClorox())
    print(getVegetables())
    print(getRaid())
    print(getButter())
    print(getLysol())
    print("Now let's clean the fridge!")
    cleanTop()
    cleanShelves()


if __name__ == "__main__":
    main()
