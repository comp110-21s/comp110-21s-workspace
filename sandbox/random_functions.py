"""Some demonstrations of randomness."""

__author__ = "Kris Jordan"

from random import random, randint

# The random function produces a random float
# between 0.0 and 1.0, not inclusive of 1.0
random_float: float = random()
print("A random_float: " + str(random_float))

# The randint function produces a random int
# between the given arguments, inclusive of 
# the second argument.
random_int: int = randint(0, 100)
print("A random int: " + str(random_int))