def add():
    spisok_stud=["Ник","Рома"]
    addC = int(input(" 1.Добавить ученика \n 2.Удалить учника \n 3.Вывести весь список \n 4.Найти номер ученика \n Введите номер команды: "))
    if addC == 1:
        students = input("Введите ученика")
        spisok_stud.append(students)
        print(spisok_stud)
    if addC == 2:
        students = input ("Введите ученика")
       
        try:
            students=int(students)
            spisok_stud.pop(students)
        except:
            a = spisok_stud.index(students)
            spisok_stud.pop(a)
        print(spisok_stud)
    if addC == 3:
        print(spisok_stud)
    if addC == 4:
        students = input ("Введите ученика")
        print(spisok_stud.index(students))
        


       
add()    
    
