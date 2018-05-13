import csv

with open('test.csv','r+') as cfile:
    reader = csv.DictReader(cfile)
    for row in reader:
        print(row['name'],row['numbers'],row['text'])

    cfile.close()










    '''
    reader = csv.reader(cfile)
    
    headers = next(reader)

    for row in reader:
        row[2] = 'test'
        print(row)    
    print(headers)
    cfile.close()







    
                  
    
'''



























    '''
    writer = csv.writer(cfile,delimiter=";")
    writer.writerow([1,2,3,4])
    writer.writerow([1,2,3,4])
    writer.writerows([['egg1','egg2'],['spamm1','spamm2']])
    cfile.close()
    '''
