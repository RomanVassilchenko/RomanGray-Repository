import csv

with open("contacts.csv", 'r+') as cfile:
    reader = csv.DictReader(cfile)
    for row in reader:
        print(row['name'],row['numbers'])
    cfile.close()


with open("contacts2.csv", 'r+') as cfile:
    reader = csv.reader(cfile)
    headers = next(reader)
    for row in reader:
        print(row)
    cfile.close()
    '''
    writer = csv.DictWriter(cfile,delimiter = ';',fieldnames = dicts.keys())
    writer.writerow(dicts)
    # writer.writerows([['q1','q2'],['q3','q4']]) Вывести массив
    cfile.close()
    '''
