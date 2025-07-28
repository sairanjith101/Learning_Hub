data = "Python is fun."

with open('file_4.txt', 'a') as file:
    file.writelines(data + '\n')