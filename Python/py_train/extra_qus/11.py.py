arr = [16, 6, 8, 4, 144]
output = []

for i in arr:
    x = i ** 0.5
    if x == int(x):
        output.append(i)

print(output)
