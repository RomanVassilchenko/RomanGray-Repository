import telebot
import config

bot = telebot.TeleBot(config.token)

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
        for i in range(0 , len(spisok_stud)):
            bot.send_message(message.chat.id, spisok_stud[i])
    if(message.text == "Города"):
        for i in range(0 , len(spisok_town)):
            bot.send_message(message.chat.id, spisok_town[i])
    if(message.text == "Достопримечательности"):
        for i in range(0 , len(spisok_dostorim)):
            bot.send_message(message.chat.id, spisok_dostoprim[i])
    if(message.text == "Удалить Студента"):
        spisok_stud.pop(len(spisok_stud) - 1)
        bot.send_message(message.chat.id, "OK")
        
        
if __name__ == '__main__':
    bot.polling(none_stop = True)

    
