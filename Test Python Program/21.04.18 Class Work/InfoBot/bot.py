# Подключаем конфиг с той же папки 
import config
# Подключаем библиотеку для работы с ботом
import telebot
#Подключаем библиотеку для работы с запросами
import requests
#Подключаем библиотеку для работы с форматом json
import json
#Подключаем библиотеку для работы с датой и временем
from datetime import datetime
#Модуль библиотеки телебот для создания кнопок
from telebot import types

#Создаем обьект класса TeleBot
bot = telebot.TeleBot(config.token)

#Функци возвращает текущее время для записи времени в лог
def get_Time_Now():
    return(datetime.strftime(datetime.now(), "%d.%m.%y %H:%M:%S"))

#Функция создает и дополняет файл лога в папке с ботом на каждое действие
def write_To_Log(mid,text):
    with open("log.txt", "a+", encoding= "utf-8" ) as lfile:
        lfile.write(get_Time_Now() + " " + str(mid) + ' ' + text + '\n')
        lfile.close()

#Обработчик команды /start
@bot.message_handler(commands = ['start'])
def start(message):
    #Приветствие бота
    bot.send_message(message.chat.id, "Хай. Ты у Инфобота")
    #Вводим в лог, что пользователь ввел /start
    write_To_Log(message.from_user.id, "user send start bot answer 'Хай. Ты у Инфобота'")
    #Создаем список кнопок и делаем так, чтобы она сама подгоняла размер кнопок
    buttons = types.ReplyKeyboardMarkup(resize_keyboard = True)
    #Добавляем названия кнопок
    buttons.add(*[types.KeyboardButton(name) for name in ["Курс валют", "Погода"]])
    #Выводим подсказку и кнопки
    bot.send_message(message.chat.id, "Выберите вариант: ", reply_markup = buttons)   
    #Обращаемся к обработчику кнопок choise_User
    bot.register_next_step_handler(message, choise_User)
def choise_User(message):
    if message.text == 'Курс валют':
        write_To_Log(message.from_user.id, "user Получил курс")
        get_Kurs(message)
    if message.text == 'Погода':
        write_To_Log(message.from_user.id, "user Получил погоду")
        get_Weather(message)
        
def get_Kurs(message):
    try:
        
        response = requests.get("http://data.egov.kz/api/v2/valutalar_bagamdary4/v302?source={\"size\":200}")
        jsonAnswer = json.loads(response.text)
        bot.send_message(message.chat.id, "Курс валют на " + get_Time_Now())
        for i in jsonAnswer:
            if i['kod'] == 'RUB' or i['kod'] == 'EUR' or i['kod'] == 'USD':
                bot.send_message(message.chat.id, "1 " + i['name_rus'] + ' = ' + i['kurs'] + ' ' + i["edinica_izmerenia"])
        write_To_Log(message.from_user.id, "Бот отправил курс")
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Сервис недоступен. Попробуйте позже")
        write_To_Log(message.from_user.id, "Бот не отправил курс т.к сайт не работает")
        bot.register_next_step_handler(message, choise_User)


def get_Weather(message):
    try:
        city = "Astana"
        data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+'&APPID=c88c03e0d228641b89c36a1b48937bb7')
        bot.send_message(message.chat.id,int(data.json()['main']['temp_min']-273) + " градусов в Астане")
        write_To_Log(message.from_user.id, "Бот отправил погоду")
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Сервис недоступен. Попробуйте позже")
        write_To_Log(message.from_user.id, "Бот не отправил курс т.к сайт не работает")
        bot.register_next_step_handler(message, choise_User)
         
#Проверка работоспособности бота
try:
    bot.polling(none_stop = True)
except:
    write_To_Log("","bot polling error")
    
