import csv

with open('test.csv', 'r', encoding="utf-8") as cfile:
    reader = csv.reader(cfile)
    headers = next(reader)
    for row in reader:
        print(row)
