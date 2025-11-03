def findint(arr):
    output = []
    for i in arr:
        if type(i) == int:
            output.append(i)
    return output

arr = [1, 2, 'a', 'b', '3', 'c', '4', 'd', 5]

print(findint(arr))