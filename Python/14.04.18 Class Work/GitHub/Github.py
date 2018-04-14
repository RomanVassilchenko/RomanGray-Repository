import requests
import json

with open("config.json",'r', encoding = "utf-8") as jfile:
    data = json.load(jfile)
    jfile.close()
    data_req = requests.get("https://api.github.com/user/repos",
                            auth=(data["username"],data["password"]))
    print(data_req.json())
    #print(data_req.json()['avatar_url'])
    
