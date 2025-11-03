from collections import Counter

nums = [10, 20, 10, 20, 30, 10]
new_num = Counter(nums)

# Find the maximum frequency
max_freq = max(new_num.values())  # Get highest frequency


most_frequent_numbers = []
# Find numbers with max frequency
for key, value in new_num.items():
    if value == max_freq:
        most_frequent_numbers.append(key)

# Get the minimum among them
print(min(most_frequent_numbers))

