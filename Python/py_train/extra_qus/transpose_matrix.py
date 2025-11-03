arr1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

transpose = []
for i in range(len(arr1[0])):
    row = []
    for j in range(len(arr1)):
        row.append(arr1[j][i])
    transpose.append(row)
print(transpose)
