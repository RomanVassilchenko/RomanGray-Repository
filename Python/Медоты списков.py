spisok_stud = ["Лена", "Катя"]
spisok_stud.append("Никита") # Добавить в конец списка
print(spisok_stud)
spisok_stud.append("Роман")
print(spisok_stud)
spisok_stud.extend(["Еркебулан", "Кирилл"]) # Добавить коллекцию в конец списка
print(spisok_stud)
spisok_stud.insert(1, "Стас") # Кинуть Стаса на 1 индекс (другие сдвигаются)
print(spisok_stud)
print(spisok_stud.index("Катя")) # Какой у 'Катя' Индекс
print(spisok_stud.index("Роман"))
spisok_stud.append("Катя")
spisok_stud.count("Катя") # Сколько 'Катя' в списке
print(spisok_stud.pop(2)) # Выводит Катя и удаляет из коллекции
