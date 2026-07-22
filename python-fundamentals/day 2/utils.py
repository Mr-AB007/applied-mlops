# utils.py
def is_even(n: int) -> bool:
    return n % 2 == 0

def factorial(n: int) -> int:
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
