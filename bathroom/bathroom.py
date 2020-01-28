#!/usr/bin/env python3

import os.path
from pathlib import Path

def getToilet():
    return "Toilet"

def getShower():
    return "Shower"

def getSink():
    return "Sink"

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    print(getToilet())
    print(getShower())
    print(getSink())

if __name__ == "__main__":
    main()
