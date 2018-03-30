otdel = ["Руководство", "Администрация" , "Бугалтерия" , "Отдел продаж" , "Программисты"]
party = ["Новый год", "8 марта" , "Наурыз" ,  "7 мая" , "День столицы"]
RealDay = [2 , 2 , 3 , 3 , 1]
day = [2 , 2 , 3 , 3 , 1]
myotdel = int(1)
myparty = int(1)

def DayOfParty(myotdel, day):
    if(myotdel == 1):
        for i in range(0 , 5):
            if(day[i] > 2):
                day[i] -= 2
    if(myotdel == 2):
        for i in range(0 , 5):
            if(day[i] > 1):
                day[i] -= 1
    if(myotdel == 3):
        for i in range(0 , 5):
            day[i] = day[i]
    if(myotdel == 4):
        for i in range(0 , 5):
            if(day[i] < 3):
                day[i] += 1
    if(myotdel == 5):
        for i in range(0 , 5):
            day[i] = day[i] + 1
        
print("Введите праздник: \n1. Новый Год \n2. 8 марта \n3. Наурыз \n4. 7 мая \n5. День столицы")
while(True):
    try:
        myparty = int(input())
        break
    except:
        continue
        
print("Введите отдел: \n1. Руководство  \n2. Администрация  \n3. Бугалтерия  \n4. Отдел Продаж  \n5. Программисты")
while(True):
    try:
        myotdel = int(input())
        break
    except:
        continue

DayOfParty()

if(myparty == 1):
    print(otdel[myotdel - 1], "на", party[myparty - 1], "отдыхает",day[myparty - 1], "дня. Официальное количество выходных:", RealDay[myparty - 1])
if(myparty == 2):
    print(otdel[myotdel - 1], "на", party[myparty - 1], "отдыхает",day[myparty - 1], "дня. Официальное количество выходных:", RealDay[myparty - 1])
if(myparty == 3):
    print(otdel[myotdel - 1], "на", party[myparty - 1], "отдыхает",day[myparty - 1], "дня. Официальное количество выходных:", RealDay[myparty - 1])
if(myparty == 4):
    print(otdel[myotdel - 1], "на", party[myparty - 1], "отдыхает",day[myparty - 1], "дня. Официальное количество выходных:", RealDay[myparty - 1])
if(myparty == 5):
    print(otdel[myotdel - 1], "на", party[myparty - 1], "отдыхает",day[myparty - 1], "дня. Официальное количество выходных:", RealDay[myparty - 1])
