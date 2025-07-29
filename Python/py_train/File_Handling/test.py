import csv

with open('data.csv', 'r') as file:
    lines = file.readlines()
    reader = csv.reader(lines)
    for r in reader:
        print(r)