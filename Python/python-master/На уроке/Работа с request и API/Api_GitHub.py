import requests
import json


with open('config.json','r') as jfile:
    data = json.load(jfile)
    data = requests.get('http://api.github.com/user',auth=(data['username'],data['password']))
