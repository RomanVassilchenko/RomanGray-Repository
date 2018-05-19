import requests
import json

with open('config.json','r') as jfile:
    data = json.load(jfile)
    jfile.close()
    data_req = requests.get('http://api.github.com/user/repos',auth =(data['Username'],data['Password']))

    print(data_req.json())
