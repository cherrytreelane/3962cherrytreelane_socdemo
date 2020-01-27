#!/usr/bin/env python3

import os.path
from pathlib import Path

def getToilet():
    print("Toilet")

def getShower():
    print("Shower")

def getSink():
    print("Sink")

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getToilet()
    getShower()
    getSink()

if __name__ == "__main__":
    main()
