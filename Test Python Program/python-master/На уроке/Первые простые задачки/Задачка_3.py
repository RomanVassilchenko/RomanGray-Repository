iq = 10
todayDay = 10
todayMonth = 3
todayYear = 2018
print ("Today is 10/03/2018")

while iq>0:
        day = int(input("Введите день"))
        month = int(input("Введите месяц"))
        year = int (input("Введите год"))
        if day >31 or day <0 or month >12 or month < 1 or year<1: 
            print("Вы введи неккоректную дату")
        else:
            print ("OK")
        if day==todayDay and month==todayMonth and year == todayYear:
            print ("Вы ввели сегодняшнюю дату\n")
            
            
            
        
