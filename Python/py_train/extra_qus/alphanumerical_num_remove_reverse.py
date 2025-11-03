user_input = input("Enter an alphanumeric value: ")
for char in user_input:
    if char.isdigit():
        user_input = user_input.replace(char, '', 1)
        break

reversed_input = user_input[::-1]
print("Output:", reversed_input)