import config
import requests
import telebot
import json
import wikipedia
import math
import sqlite3
from datetime import datetime
from telebot import types

info = list()

def get_from_DB(sql):
	conn = sqlite3.connect("bot.db")
	cursor = conn.cursor()
	cursor.execute(sql)
	return cursor.fetchall()
	conn.close()


def oper_with_DB(sql):
	conn = sqlite3.connect("bot.db")
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()


def get_Time_Now():
	return datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")


def write_To_Log(mid, text):
	with open("log.txt", "a+", encoding='utf-8') as flog:
		flog.write(get_Time_Now() + " " + str(mid) + " " + text + "\n")


bot = telebot.TeleBot(config.token)
write_To_Log("", "bot started!")


@bot.message_handler(commands=["start"])
def start(message):

	bot.send_message(message.chat.id,
	    get_from_DB("SELECT * FROM text_from_user")[0][1])
	bot.send_message(message.chat.id,
	    get_from_DB("SELECT * FROM text_from_user")[1][1])
	bot.register_next_step_handler(message, start)

    global info
    info.append(message.text)
	bot.send_message(message.chat.id,
	                 get_from_DB("SELECT * FROM text_from_user")[2][1])
	bot.register_next_step_handler(message, start)
	age = message.text
	status = 0
	uid_telegram = message.chat.id
	get_num(message)


def get_num(message):
	bot.send_message(message.chat.id,
	                 get_from_DB("SELECT * FROM text_from_user")[3][1])
	buttons = types.InlineKeyboardMarkup()
	buttons = types.ReplyKeyboardMarkup(
	    resize_keyboard=True, one_time_keyboard=True)
	buttons.add(type.KeyboardButton("Отправить номер", request_contact=True))
	bot.send_message(
	    message.chat.id,
	    get_from_DB("SELECT text FROM text_for_user WHERE id = 1" [0]),
	    reply_markup=buttons)
	bot.register_next_step_handler(message, get_location)


def get_location(message):
	bot.send_message(message.chat.id,
	                 get_from_DB("SELECT * FROM text_from_user")[4][1])
	buttons = types.ReplyKeyboardMarkup(
	    resize_keyboard=True, one_time_keyboard=True)
	buttons.add(
	    type.KeyboardButton("Отправить локацию", request_location=True))
	bot.send_message(
	    message.chat.id,
	    get_from_DB("SELECT text FROM text_for_user WHERE id = 1" [0]),
	    reply_markup=buttons)
	registered_date = get_Time_Now()
	oper_with_DB(
	    "INSERT INTO Название таблицы VALUES (name, uid_telegram, status, number , adress, age, registered_age)"
	    % message.text)

	#print(get_from_DB("SELECT * FROM text_from_user")[0][0])
# oper_with_DB("INSERT INTO Название таблицы VALUES (NULL, 'Это текст с питона')") Добавляет


# oper_with_DB("INSERT INTO Название таблицы VALUES (NULL, '%s')" % message.text) Добавляет
# open_with_DB("DELETE  FROM Название таблицы") Удалит все, что в таблицы
# open_with_DB("DELETE  FROM Название таблицы WHERE id=%i" %id)
# open_with_DB("UPDATE Название таблицы SET text = 'Это измененный текст' WHERE id = id2" %id2)

try:
	bot.polling(none_stop=True)
except:
	write_To_Log("", "error bot polling")
