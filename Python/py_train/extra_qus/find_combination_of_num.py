from itertools import combinations

arr = [4, 4, 5, 3]
total = 8

comb = combinations(arr, 2)

output = 0
valid_pairs = []  # Store valid pairs

for c in comb:
    print(c)  # Print all pairs
    if sum(c) == total:
        output += 1
        valid_pairs.append(c)  # Store valid pair

print("Total Pairs:", output)
print("Valid Pairs:", valid_pairs)
