import csv
dicts = {'Contact':['A','B'], "number":['1234','346']}
with open("contacts.csv", 'r+') as cfile:
    reader = csv.reader(cfile)
    headers = next(reader)
    for row in reader:
        row[2] = 'test'
        print(row)
    cfile.close()
    '''
    writer = csv.DictWriter(cfile,delimiter = ';',fieldnames = dicts.keys())
    writer.writerow(dicts)
    # writer.writerows([['q1','q2'],['q3','q4']]) Вывести массив
    cfile.close()
    '''
