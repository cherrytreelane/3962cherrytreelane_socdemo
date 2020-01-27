#!/usr/bin/env python3

import os.path
from pathlib import Path

def getBed():
    print("Bed")

def getNightStand():
    print("Night stand")

def main():
    print("The %s contains:" % Path(os.path.basename(__file__)).stem)
    getBed()
    getNightStand()

if __name__ == "__main__":
    main()
