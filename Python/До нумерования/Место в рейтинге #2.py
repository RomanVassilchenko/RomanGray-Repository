Name = ["Никулин", "Карпов" , "Смит" , "Васильченко" , "Лайков" , "Васечкин" , "Петров" , "Иванов"]
Bal = [12, 11.5 , 11 , 10.5 , 10, 9.5 , 9, 8.5]
Mesto = [1, 2, 3, 4, 5, 6, 7, 8]

Mynames = input("Введите фамилию ")

print(Name[Name.index(Mynames)],": место в рейтинге:",Mesto[Name.index(Mynames)],", а баллов:",Bal[Name.index(Mynames)])
