#!/usr/bin/env python3

import os.path
from pathlib import Path

def getCouch():
    print("Couch")

def getCoffeeTable():
    print("Coffee table")

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getCouch()
    getCoffeeTable()

if __name__ == "__main__":
    main()
