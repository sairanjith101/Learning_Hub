from collections import defaultdict

d = defaultdict(list)

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eve", "B"),
    ("Frank", "A")
]

for name,grade in students:
    d[grade].append(name)

print(d)