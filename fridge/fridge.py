#!/usr/bin/env python3

import os.path
from pathlib import Path

def getMilk():
    print("Milk")

def getEggs():
    print("Eggs")

def getVegetables():
    print("Vegetables")

def getButter():
    print("Butter")

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getMilk()
    getEggs()
    getVegetables()
    getButter()
    

if __name__ == "__main__":
    main()
