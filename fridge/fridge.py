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

if __name__ == "__main__":
    main()
