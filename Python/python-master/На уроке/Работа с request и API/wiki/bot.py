import config
import requests
import telebot
import json
import wikipedia
import math
from datetime import datetime
from telebot import types

def get_Time_Now():
    return datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

def write_To_Log(mid, text):
    with open("log.txt", "a+", encoding='utf-8') as flog:
        flog.write(get_Time_Now()+" "+str(mid)+" "+text+"\n")

bot = telebot.TeleBot(config.token)
write_To_Log("", "bot started!")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Здравствуй, друг.")
    write_To_Log(message.from_user.id, "user send start command and bot send hello friend")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in["Узнать слово","Перевести слово", "Узнать погоду", "Курс валют", "Отследить посылку"]])
    bot.send_message(message.chat.id, "", reply_markup=keyboard)
    write_To_Log(message.from_user.id, "bot send message with buttons")
    bot.register_next_step_handler(message, choise_User)
    print('ok')
def choise_User(message):
    print('ok')
    if message.text == "Перевести слово":
        bot.send_message(message.chat.id, "Введите слово: ")
        write_To_Log(message.from_user.id, "user write word for translate text")
        bot.register_next_step_handler(message, translate_Word)
    elif message.text == "Узнать слово":
        bot.send_message(message.chat.id, "Введите слово: ")
        write_To_Log(message.from_user.id, "user write word for search text")
        bot.register_next_step_handler(message, search_Word)
    elif message.text == "Узнать погоду":
        bot.send_message(message.chat.id, "Введите город: ")
        write_To_Log(message.from_user.id, "user write city for get weather")
        bot.register_next_step_handler(message, get_Weather)
    elif message.text == "Курс валют":
        write_To_Log(message.from_user.id, "user get Kurs")
        get_Kurs(message)
    elif message.text == "Отследить посылку":
        bot.send_message(message.chat.id, "Введите трек номер: ")
        write_To_Log(message.from_user.id, "user write track numbr for get post")
        bot.register_next_step_handler(message, get_Track_Post)

def translate_Word(message):
    try:
        response =requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate",
                            data={"key":"trnsl.1.1.20180420T210650Z.b4f0c6d8761f545a.dd00945f6cc450e3c34557301839925ead673187",
                                  "text":message.text,
                                  "lang":"en-ru"})
        jsonAnswer = json.loads(response.text)
        bot.send_message(message.chat.id, jsonAnswer["text"])
        write_To_Log(message.from_user.id, "user write "+message.text+" bot send answer "+str(jsonAnswer["text"][0]))
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Переводчик недоступен. Попробуй позже.")
        write_To_Log(message.from_user.id, "user not translate word "+message.text)
        bot.register_next_step_handler(message, choise_User)

def search_Word(message):
    try:
        wikipedia.set_lang("ru")
        bot.send_message(message.chat.id, wikipedia.summary(message.text))
        write_To_Log(message.from_user.id, "user write "+message.text+" bot answer "+wikipedia.summary(message.text))
        bot.register_next_step_handler(message, choise_User)
    except wikipedia.exceptions.DisambiguationError as e:
        bot.send_message(message.chat.id, wikipedia.summary(e.options[0]))
        write_To_Log(message.from_user.id, "user write "+message.text+" bot answer "+wikipedia.summary(e.options[0]))
        bot.register_next_step_handler(message, choise_User)

def get_Weather(message):
    try:
        response =requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate",
                            data={"key":"trnsl.1.1.20180420T210650Z.b4f0c6d8761f545a.dd00945f6cc450e3c34557301839925ead673187",
                                  "text":message.text,
                                  "lang":"ru-en"})
        jsonAnswer = json.loads(response.text)
        data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+str(jsonAnswer["text"][0])+"&APPID=6e544f6c9bf7e9ba93af07066baf396a")
        temp = round(data.json()["main"]["temp"]-273.15)
        toUser = "Погода в "+message.text+" : "+str(temp)+"C"
        bot.send_message(message.chat.id, toUser)
        write_To_Log(message.from_user.id, "user write "+message.text+" bot send answer "+toUser)
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Погода или переводчик недоступны. Попробуй позже.")
        write_To_Log(message.from_user.id, "user not get weather for "+message.text)
        bot.register_next_step_handler(message, choise_User)

def get_Kurs(message):
    try:
        response = requests.get("http://data.egov.kz/api/v2/valutalar_bagamdary4/v302?source={\"size\":200}")
        jsonAnswer = json.loads(response.text)
        bot.send_message(message.chat.id, "Курс валют на "+get_Time_Now())
        for i in jsonAnswer:
            if i["kod"] == "RUB" or i["kod"] == "USD" or i["kod"] == "EUR":
                bot.send_message(message.chat.id, "1 "+i["name_rus"]+" = "+i["kurs"]+" "+i["edinica_izmerenia"])
        write_To_Log(message.from_user.id, "bot send kurs")
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Портал недоступен. Попробуйте позже.")
        write_To_Log(message.from_user.id, "user not get Kurs ")
        bot.register_next_step_handler(message, choise_User)

def get_Track_Post(message):
    try:
        response = requests.get("https://post.kz/external-api/tracking/api/v2/"+message.text)
        lastLocation = response.json()["last"]
        bot.send_message(message.chat.id, lastLocation["date"]+" "+lastLocation["city"]+" "+lastLocation["dep_name"]+" "+lastLocation["address"])
        bot.send_message(message.chat.id, "Получатель: "+response.json()["receiver"]["name"])
        write_To_Log(message.from_user.id, "user get info for port with num "+message.text+" on date and address "+lastLocation["date"]+" "+lastLocation["city"]+" "+lastLocation["dep_name"]+" "+lastLocation["address"])
        bot.register_next_step_handler(message, choise_User)
    except:
        bot.send_message(message.chat.id, "Портал недоступен. Попробуйте позже.")
        write_To_Log(message.from_user.id, "user not get post info with num "+message.text)
        bot.register_next_step_handler(message, choise_User)

try:
    bot.polling(none_stop = True)
except:
    write_To_Log("", "error bot polling")
