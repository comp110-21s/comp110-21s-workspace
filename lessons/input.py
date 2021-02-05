"""A program to demonstrate user input and variables."""

name: str = input("Who are you? ")
print("Wow, " + name + ", you rock!")
print(name + "have a great day!")

a: str = "a"
b: str = "b" + a + "b"
c: str = "c" + b + "c"
n: int = len(c)
print(c[n-1])
print(n)
