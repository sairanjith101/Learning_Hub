
def findsumofseries(n):
    output = 0
    for i in range(0, n+1):
        output += i
    
    return output

n = int(input("Enter a value: "))

print(findsumofseries(n))