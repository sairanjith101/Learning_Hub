n = int(input("Enter a number: ")) 

def fibonacci_series(n):
    fib_ser = []
    a,b = 0,1
    for i in range(n):
        fib_ser.append(a)
        a,b = b, a + b
    return fib_ser

print(fibonacci_series(n))