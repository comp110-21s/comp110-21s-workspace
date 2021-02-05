"""An exercise in remainders and boolean logic."""

__author__ = "730403391"


number: int = int(input("Pick an int "))
if (number % 2) == int(0) and (number % 7) == int(0): 
    print("TAR HEELS")
else:
    if (number % 2) == int(0):
        print("TAR")
    else:
        if (number % 7) == int(0):
            print("HEELS")
        else:
            print("CAROLINA")
