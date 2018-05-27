#Подключаемм конфиг с той же папки с токеном бота
import config
#Подключаем библиотеку для работы с ботом
import telebot
#Подключаем библиотеку для получения курса
import requests
#Подключаем библитеку для работы с датой и временем
from datetime import datetime
#Модуль библиотеки telebot для создания кнопок
from telebot import types
#Подключаем библиотеку для работы с форматом json
import json
#Подключаем библиотеку для работы с wikipedia
import wikipedia

#Создаем объект класса Telebot
bot = telebot.TeleBot(config.token)






#Функция возвращает текущее время, служит для записи времени в лог
def get_Time_Now():
    return datetime.strftime(datetime.now(),"%d.%m.%Y %H:%M:%S")
#Функция создает и дополняет файл лога в папке с ботом на каждое действие
def write_To_Log(mid,text):
    with open('log.txt','a+',encoding = "utf-8") as lfile:
        lfile.write(get_Time_Now() + ' ' + str(mid)+ " " + text+'\n')
        lfile.close()


#Обработчик команды /start
@bot.message_handler(commands = ['start'])
def start(message):

    wikipedia.set_lang('ru')


    
    bot.send_message(message.chat.id,"Привет, и, О склонись простой юзер")
    write_To_Log(message.from_user.id,'user send start')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard = True)
    buttons.add(*[types.KeyboardButton(name) for name in ['Помощь на экзамене','Курс Валют','Погода']])
    bot.send_message(message.chat.id,'Выберите вариант',reply_markup=buttons)
    bot.register_next_step_handler(message,choise_User)
    

def choise_User(message):
    
    if message.text == "Курс Валют":
        write_To_Log(message.from_user.id,"user get kurs")
        get_Kurs(message)

    elif message.text =="Помощь на экзамене":
        write_To_Log(message.from_user.id,'user search word')
        bot.send_message(message.chat.id,'Введите слово')
        bot.register_next_step_handler(message,search_Word)
    
    elif message.text == "Погода":
        write_To_Log(message.from_user.id,"user get weather")
        bot.send_message(message.chat.id,"Введите город")
        bot.register_next_step_handler(message,search_Weather)
    else:
        bot.register_next_step_handler(message,choise_User)
        

def search_Weather(message):
    city = message.text
    data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=58457cb0014568039f79584ed7dc67ca')
    bot.send_message(message.chat.id,int(data.json()['main']['temp_min']-273))
    bot.register_next_step_handler(message,choise_User)

def search_Word(message):
    try:        
        wikiresult = wikipedia.summary(message.text)
        bot.send_message(message.chat.id,wikiresult)
        write_To_Log(message.from_user.id,'user search word'+ message.text+ 'bot answer' + wikiresult)
        bot.register_next_step_handler(message,choise_User)
    except wikipedia.exceptions.DisambiguationError as e:
        wikiresult = wikipedia.summary(e.options[0])
        bot.send_message(message.chat.id,wikiresult)
        write_To_Log(message.from_user.id,'user search word'+ message.text+ 'bot answer' + wikiresult)
        bot.register_next_step_handler(message,choise_User)
    except wikipedia.exceptions.PageError:      
        bot.send_message(message.chat.id,"Данного слова не существует")
        write_To_Log(message.from_user.id,'user search word'+ message.text+ 'bot answer' )
        bot.register_next_step_handler(message,choise_User)
    except:
        bot.send_message(message.chat.id,'Cервис не Доступен')
        write_To_Log(message.from_user.id,'wiki not working')
        bot.register_next_step_handler(message,choise_User)
        

def get_Kurs(message):
    try:
        
        response = requests.get('http://data.egov.kz/api/v2/valutalar_bagamdary4/v302?source={"size":200}')
        jsonAnswer = json.loads(response.text)
        bot.send_message(message.chat.id,"Курс на "+get_Time_Now())
        for i in jsonAnswer:
            if i["kod"] == "RUB" or i["kod"] =="USD":
                bot.send_message(message.chat.id,"1 " + i ["name_rus"] + " = " + i['kurs'] +" "+i["edinica_izmerenia"])
        write_To_Log(message.from_user.id,"bot send kurs")
        bot.register_next_step_handler(message, choise_User)
    except:
        print("1")
        bot.send_message(message.chat.id,"Сервис не работает")
        write_To_Log(message.from_user.id,'bot not send kurs becouse portal not working')
        bot.register_next_step_handler(message,choise_User)
                



#Проверка работоспособности бота
try:
    bot.polling(none_stop = True)
    
except:
    write_To_Log('','bot polling error')


#type() - узнать тип переменной
