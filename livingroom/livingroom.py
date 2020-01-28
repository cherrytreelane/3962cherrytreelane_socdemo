#!/usr/bin/env python3

import os.path
from pathlib import Path

def getCouch():
    return "Couch"

def getCoffeeTable():
    return "Coffee table"

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    print(getCouch())
    print(getCoffeeTable())

if __name__ == "__main__":
    main()
