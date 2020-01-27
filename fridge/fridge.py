#!/usr/bin/env python3

import os.path
from pathlib import Path

import sys
sys.path.append('..')
from thecloset.cleaning_products import *

def getMilk():
    print("Milk")

def getEggs():
    print("Eggs")

def getVegetables():
    print("Vegetables")

def getButter():
    print("Butter")

def cleanTop():
    print("You cleaned the top of the fridge using " + getClorox())

def cleanShelves():
    print("You cleaned the shelves of the fridge using " + getLysol())

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getMilk()
    getEggs()
    getVegetables()
    getButter()
    print("Now let's clean the fridge!")
    cleanTop()
    cleanShelves()

if __name__ == "__main__":
    main()
