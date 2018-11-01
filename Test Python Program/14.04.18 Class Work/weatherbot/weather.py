import requests

city = input("Введите город на англиском: ")
data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+'&APPID=c88c03e0d228641b89c36a1b48937bb7')
print("Минимальная температура в "+city+":",int(data.json()['main']['temp_min']-273))
print("Максимальная температура в "+city+":",int(data.json()['main']['temp_max']-273))
