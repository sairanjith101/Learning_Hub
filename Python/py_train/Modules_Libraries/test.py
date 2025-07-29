import math

def sqrt(n):
    if n < 0:
        raise ValueError("Value must be positive")
    return math.sqrt(n)

try:
    n = int(input("Enter value: "))
    print("Squar Value: ", sqrt(n))
except ValueError as ve:
    print("Value Error: ", ve)