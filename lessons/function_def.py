"""How to define a funtion"""

def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b

result: int = (my_max(10 + 1, 10))
print(result)
