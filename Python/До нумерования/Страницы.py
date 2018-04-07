page = 1
docs = int(input("Введите количество листов "))
if(docs < 0):
    print ("ERROR")
else:
    while page <= docs:
            print("Начало печати страницы", page)
            print("Подача бумаги")
            print("Нанесение краски")
            print("Вывод бумаги")
            page  += 1
    print("Печать завершена")
