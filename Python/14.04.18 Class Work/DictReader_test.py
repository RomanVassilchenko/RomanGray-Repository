import csv

with open('test.csv', 'r', encoding="utf-8") as cfile:
    reader = csv.DictReader(cfile)
    #for row in reader:
    #    print(row['id'])
    rows = list(reader)
    print(rows[2]['name'])
    
