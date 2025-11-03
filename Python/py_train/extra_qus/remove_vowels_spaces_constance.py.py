text = "Remove vowels 123 from this text"

vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "i", "O", "U"]

spaces = [" "]

res = []

for i in text:
    if i not in vowels:
        if i not in spaces:
            if i.isalpha():
                res.append(i)

output = "".join(res)
print(output)