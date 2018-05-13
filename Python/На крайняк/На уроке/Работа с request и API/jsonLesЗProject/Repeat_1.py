import json

def write_to_JSON(data,filename):
    with open(filename,'w',encoding = 'utf-8') as jfile:
        jfile.write(json.dumps(data,ensure_ascii = False,indent = 4))
        jfile.close()
filename = input('Введите название файла: ')
data = {'login':'Test1','password':'654321'}
write_to_JSON(data, filename)















'''
import json

def write_to_json(name, date, city):
    with open('config.json','r') as jfr:
        jf_file = json.load(jfr)
    with open('config.json','w') as jf:
        jf_target = jf_file[0]['users']
        user_info = {'name': name, 'date': date, 'city': city}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=4)

write_to_json('foo', 'bar', 'baz')
'''


























'''
import csv

with open('test.csv','r') as cfile:
    reader = csv.DictReader(cfile)
    rows = list(reader)
    print(rows[0]['name'])
'''
        


'''
with open('new.txt','w') as f:
    f.write("
Test
Proverka
Repeat
")
'''
