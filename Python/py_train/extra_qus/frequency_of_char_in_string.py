s = "abbcccddddeeeee"

output = {}

for i in s:
    if i not in output:
        output[i] = 1
    else:
        output[i] += 1

print(output)