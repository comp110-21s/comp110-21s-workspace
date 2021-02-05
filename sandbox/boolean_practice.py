"""Bolean practice"""

how_much: int = int(input("Choose a number between 0 and 100: "))
if how_much < 10:
    print("red")
    if how_much < 5:
        print("light red")
else:
    if how_much < 20: 
        print("orange")
    else: 
        if how_much < 30: 
            print("yellow")

print("after")
if how_much == 10:
    print("green")

v: int = 7
b: int = 8

d: bool = v > 10 and b < 25
name: str = str(input("What is your name?"))
if name == "aryonna": 
    print("hey girl")
else: 
    print("no comment")
