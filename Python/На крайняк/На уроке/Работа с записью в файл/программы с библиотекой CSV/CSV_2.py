import csv

with open('nite.csv','r+') as cfile:
    reader = csv.reader(cfile)
    headers = next(reader)
    for row in reader:
        print(row)

    cfile.close()
