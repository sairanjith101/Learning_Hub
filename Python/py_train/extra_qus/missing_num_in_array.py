def find_missing_number(n, arr):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example 1
n = 5
arr = [1, 2, 3, 5]
print(find_missing_number(n, arr))  # Output: 4

# Example 2
n = 2
arr = [1]
print(find_missing_number(n, arr))  # Output: 2


# option 2

# def find_missing_number(n: int, arr: list[int]) -> int:
#     for i in range(1, n + 1):  # Loop through 1 to n
#         if i not in arr:  
#             return i  # Return missing number immediately

# n = 7
# arr = [1, 2, 4, 5, 6, 7]

# print(find_missing_number(n, arr))  # Output: 3
