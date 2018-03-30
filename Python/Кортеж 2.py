def salat():
    chislo = int(input("Введите количество человек: "))
    Salat = ("Картофель ", 50 ,
             "Лук " , 20,
             "Колбаса " , 100 ,
             "Мойнез" , 15 ,
             "Соленые Огурцы ", 30)
    for i in range(0 , 10 + 1):
        if(i % 2 != 0):
            print(Salat[i] * chislo)
        else:
            print(Salat[i])
salat()
        
        
