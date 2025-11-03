arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

sum_of_column_1 = 0
sum_of_column_3 = 0

for i in range(len(arr)):
    sum_of_column_1 += arr[i][0]
    sum_of_column_3 += arr[i][2]

print("Sum of column 1 is: ", sum_of_column_1)
print("Sum of column 3 is: ", sum_of_column_3)

sum_of_column_2 = 1
sum_of_column_4 = 1

for i in range(len(arr)):
    sum_of_column_2 *= arr[i][1]
    sum_of_column_4 *= arr[i][3]

print("Multiple of column 2 is: ", sum_of_column_2)
print("Multiple of column 4 is: ", sum_of_column_4)