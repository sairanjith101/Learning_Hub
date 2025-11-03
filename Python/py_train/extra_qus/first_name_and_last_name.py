# option 1

import re

text = "Hello Gary Williams"

regex = r'([\w]+)\s([\w]+)\s([\w]+)'

match = re.findall(regex,text)

for i in match:
    print("First Name: ", i[1])
    print("Second Name: ", i[2])


# option 2

text = "Hello Gary Williams"

new_text = text.split()

print("First Name: ", new_text[1])
print("Second Name: ", new_text[2])