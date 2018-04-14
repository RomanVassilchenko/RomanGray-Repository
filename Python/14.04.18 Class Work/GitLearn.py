import requests
import getpass
data = requests.get("https://google.com")
password = getpass.getpass("Введите пороль: ")
