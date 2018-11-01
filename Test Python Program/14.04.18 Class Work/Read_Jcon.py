import json
def Read_JSON(text):
    with open(text, 'r') as conf_file:
        data = json.load(conf_file)
        print(data)
        conf_file.close()
a = input()
a = a + '.json'
Read_JSON(a)    
