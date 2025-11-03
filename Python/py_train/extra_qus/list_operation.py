nums = [5, 3, 8, 3, 1, 8, 2]

new_nums = []

for n in nums:
    if n not in new_nums:
        new_nums.append(n)

new_nums.sort()

print(new_nums)
print("minimum num: ", min(new_nums))
print("max num: ", max(new_nums))


mylist = list(dict.fromkeys(new_nums))
print(mylist)

# option 2

# def process_numbers(nums: list[int]) -> tuple[list[int], int, int]:
#     remove_duplicate = sorted(set(nums))  # Remove duplicates & sort
#     min_num = min(remove_duplicate)  # Find minimum
#     max_num = max(remove_duplicate)  # Find maximum
#     return remove_duplicate, min_num, max_num  # Return as tuple

# # Example usage:
# nums = [5, 3, 8, 3, 1, 8, 2]
# print(process_numbers(nums))  
