while True:
    def Add():
        Name = input("Введите фамилию ")
        Bal = input("Введите балл ")
        Mesto = input("Введите место ")
        a.append(Name)
        b.append(Bal)
        c.append(Mesto)
    a = [11 , 10 , 5 , 12 , 8 , 7 , 4 , 12]
    b = ["Никулин", "Карпов" , "Смит" , "Васильченко" , "Лайков" , "Васечкин" , "Петров" , "Иванов"]
    c = [ 1 , 2 , 4 , 3 , 5 , 6 , 7 , 8]
    D = input("Введите фамилию или Add ")
    if D == "Add":
        Add()
    else:    
        Cnt = 0
        for i in range(0 , len(a)):
            if(D == b[i]):
                Cnt = Cnt + 1

        if(Cnt > 0):
            for i in range (0, len(a)):
                if D == b[i]:
                    print(b[i],a[i] , "баллов и место в рейтинге:", c[i])
        else:
            print("Фамилии нету")
            continue
