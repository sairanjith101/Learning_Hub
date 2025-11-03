def SMPN(arr):
    output = []
    for i in range(1, max(arr)):
        if i not in arr:
            output.append(i)
    return min(output)

# arr = [-1, 1, 2, 3, 0, -2, 7, 8]
# arr = [10, 20, 1, 2]
arr = [-5, 0, 2, 10]
print(SMPN(arr))
