a = {"Казахстан": "Астана",
     "США": "Вашингтон",
     "Украина": "Киев",
     "Россия": "Москва",
     "Великобритания": "Лондон"}
print (a["Казахстан"] ,
       a["Великобритания"],
       a["Украина"],
       a["Россия"],
       a["США"])
print(a.get("Test3")) # Проверка на наличие
print(a.items()) # Все элементы
print(a.keys()) # Выводит все ключи

a.clear()
a = {"test1" : "test" , "test2" : "test"}
print(a)
a.pop("test2") #удаляет test2
print (a)
a = {"test1" : "test" , "test2" : "test"}
print(a.popitem()) # удаляет последнее значение и выводит
a = {"test1" : "test" , "test2" : "test", "test3" : "test"}
print(a.values()) # Выводит значения
a.update({"test" : "test"}) #Добавляет или изменяет Словарь
print (a)
