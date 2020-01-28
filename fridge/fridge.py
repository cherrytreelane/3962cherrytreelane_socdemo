#!/usr/bin/env python3

import os.path
from pathlib import Path

import sys
sys.path.append('..')
from thecloset.cleaning_products import *

def getMilk():
    return "Milk"

def getEggs():
    return "Eggs"

def getVegetables():
    return "Vegetables"

def getButter():
    return "Butter"

def cleanTop():
    print("You cleaned the top of the fridge using " + getClorox())

def cleanShelves():
    print("You cleaned the shelves of the fridge using " + getLysol())

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    print(getMilk())
    print(getEggs())
    print(getVegetables())
    print(getButter())
    print("Now let's clean the fridge!")
    cleanTop()
    cleanShelves()

if __name__ == "__main__":
    main()
