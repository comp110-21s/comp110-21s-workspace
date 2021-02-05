"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730403391"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint 


print("Your fortune cookie says... ")
chance: int = randint(1, 100)
if chance < 25: 
    print("Someone special will come into your life soon.")
else:
    if chance < 50:
        print("Something BIG is about to happen in your life!")
    else:
        if chance < 75:
            print("Your hard work is about to pay off.")
        else: 
            if chance <= 100:
                print("Cheer up... good things come to those who wait.")

print("Now, go spread positive vibes!")
