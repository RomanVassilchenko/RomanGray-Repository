import telebot
import config

bot = telebot.TeleBot(config.token)


otdel = ["Руководство", "Администрация" , "Бугалтерия" , "Отдел продаж" , "Программисты"]
party = ["Новый год", "8 марта" , "Наурыз" ,  "7 мая" , "День столицы"]
RealDay = [2 , 2 , 3 , 3 , 1]
day = [2 , 2 , 3 , 3 , 1]
myotdel = " "
myparty = " "
R = 1

@bot.message_handler(content_types = ["text"])
def answer_all_messages(message):
    #print(message)
    global R
    if R == 1:
        bot.send_message(message.chat.id, "Введите праздник: \n1. Новый Год \n2. 8 марта \n3. Наурыз \n4. 7 мая \n5. День столицы")
        Holiday(message)
        R = R + 1
        print(R)
    elif(R == 2):
        bot.send_message(message.chat.id, "Введите отдел: \n1. Руководство  \n2. Администрация  \n3. Бугалтерия  \n4. Отдел Продаж  \n5. Программисты")
        Otdelenie(message)
        R = R + 1
    elif(R == 3):
        DayOfParty(myotdel, day, otdel, party, RealDay, myparty)
        R = R + 1
    elif(R == 4):
        End(myotdel, day, otdel, party, RealDay, myparty)
        R = R + 1
        
        
def Holiday(message):
    
    while(True):
    
        myparty = message.text
        if(myparty == 1 or myparty == 2 or myparty == 3 or myparty == 4 or myparty == 5 ):
            break
        else:
            continue

def Otdelenie(message):
    while(True): 
        
        myotdel = message.text
        if(myotdel == 1 or myotdel == 2 or myotdel == 3 or myotdel == 4 or myotdel == 5 ):
            break
        else:
            continue

def DayOfParty(myotdel, day, otdel, party, RealDay, myparty):
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
            
def End(myotdel, day, otdel, party, RealDay, myparty):
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
        
if __name__ == '__main__':
    bot.polling(none_stop = True)

    
