#!/usr/bin/env python3

import os.path
from pathlib import Path

def getBed():
    return "Bed"

def getNightStand():
    return "Night stand"

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    print(getBed())
    print(getNightStand())

if __name__ == "__main__":
    main()
