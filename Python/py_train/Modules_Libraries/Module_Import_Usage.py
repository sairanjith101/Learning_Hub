import math

def sqrt_value(n):
    if n < 0:
        raise ValueError("Square root must be positive")
    return math.sqrt(n)

try:
    n = int(input("Enter a value: "))
    print(f"Square root: {sqrt_value(n)}")
except ValueError as ve:
    print(f"Error: {ve}")
