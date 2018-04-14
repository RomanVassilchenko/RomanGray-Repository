import json
def write_to_json(data, filename):
    with open('config.json','w' , encoding = "utf-8") as jfile:
        jfile.write(json.dumps(data,ensure_ascii = False, indent = 4))
    jfile.close()
    
data = {"login":"Test1", "password":"654321"}
filename = input("Введите название файла ") + '.'
file_format = input("Введите формат файла ")
filename = filename + fileformat
write_to_json(data, filename)
        
