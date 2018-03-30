import telebot
import config

bot = telebot.TeleBot(config.token)
len_stud = int(4)
len_town = int(9)
len_dostoprim = int(8)
spisok_stud = ["Лена", "Катя" , "Еркебулан", "Никита", "Дастан", "Влад", "Кирилл", "Стас" , "Роман"]
spisok_town = ["Алма-Ата",
               "Астана",
               "Шымкент",
               "Караганда",
               "Актобе",
               "Тараз",
               "Павлодар",
               "Усть-Каменогорск",
               "Семей"]
spisok_dostoprim = ["Байтерек", "Хан-Шатыр", "Мега", "Керуен",]
@bot.message_handler(content_types = ["text"])
def answer_all_messages(message):
    print(message)

    if(message.text == "Студенты"):
        for i in range(0 , len_stud - 1):
            bot.send_message(message.chat.id, spisok_stud[i])
    if(message.text == "Города"):
        for i in range(0 , len_town - 1):
            bot.send_message(message.chat.id, spisok_town[i])
    if(message.text == "Достопримечательности"):
        for i in range(0 , len_dostoprim - 1):
            bot.send_message(message.chat.id, spisok_dostoprim[i])
    if(message.text == "Удалить Студента"):
        spisok_stud.pop(len_stud - 1)
        bot.send_message(message.chat.id, "OK")
        len_stud = len_stud - 1
        
        
if __name__ == '__main__':
    bot.polling(none_stop = True)

    
