import config
import requests
import telebot
import json
from telebot import apihelper
from telebot import types
import sqlite3
import logging

#ip = '185.228.233.248'
#port = '1080'

#apihelper.proxy = {
#  'https': 'socks5://{}:{}'.format(ip,port)
#}


#oper_with_db("UPDATE text_for_user SET text='Это измененный текст' WHERE id=12")    -      допилить апдейт для админки обязательно исползовать условие WHERE иначе на данный текст будет заменен весь столбец

# buttons = types.InlineKeyBoardMarkup - Создание Inline кнопку
# buttons.add(*[types.InlineKeyBoardButton(name,callback_data = name) for name in ["Да","Нет"]])                 'Доп. инф.  в группе

#button.add(types)           -



bot = telebot.TeleBot(config.token)

_db_Number_of_User = 0

_db_User_Status = 0

myArray =[_db_Number_of_User,_db_User_Status]
print(myArray)


@bot.message_handler(commands = ['start'])
def start(message):
    try:
        res = cursorConnectionAndRead("SELECT Status FROM First_4_answers WHERE UserTelegrammID =%s" %message.from_user.id)
        res =int(res[0][0])
        print(res)
        if res == 1:
            userRights(message)
        elif res ==0:
            considiration(message)
    except:
        main(message)

    






def questioning(message):
    global results
    global myArray
    
    print(results)
    if results !=[]:
        for i in results:
            bot.send_message(message.chat.id,i)
            bot.register_next_step_handler(message,test)
            del results[0]
            break
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True) #one_time_keyboard=True - спрятать кнопку после нажатия
        keyboard.add(*[types.KeyboardButton(name) for name in["Отправить"]])
        bot.send_message(message.chat.id, "Если все данные верны нажмите 'Отправить', в противном случае введите данные заново нажав на /start", reply_markup=keyboard)
        
        myArray[_db_Number_of_User]=message.from_user.id
        myArray = tuple(myArray)

        bot.register_next_step_handler(message,finalStepOfRegistration)

        
    
def test(message):
    
    myArray.append(message.text)
    print(myArray)
    
    questioning(message)



    

def cursorConnectionAndRead(sql):
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    info = cursor.fetchall()
    conn.close()
    return info

def cursorConnectionAndWrite(tableName,insertingTurpleWithValues):
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor()
    cursor.execute("insert into %s values %s" %(tableName,insertingTurpleWithValues))
    conn.commit()
    conn.close()

def cursorConnectionAndUpdate(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue):
    conn = sqlite3.connect('TZ_base.db')
    cursor = conn.cursor("UPDATE %s SET %s='%s' WHERE %s=%s"%(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue))
    cursor.execute()
    conn.commit()
    conn.close()

def finalStepOfRegistration(message):
    global myArray

    if message.text == "Отправить":
        bot.send_message(message.chat.id,'Поздравляю вы прошли регистрацию, ваша заявка находится на рассмотрении администрации')

        cursorConnectionAndWrite("First_4_answers", myArray)


        #cursorConnectionAndUpdate("First_4_answers","Status",1,'UserTelegrammId',message.from_user.id)



def main(message):
    global results
    global myArray
    print('status')
    myArray = list(myArray)
    myArray = [_db_Number_of_User, _db_User_Status]

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/Users/БорсовН/Documents/GitHub/python/Дз по python/Дз8/ТЗ/myapp.log')

    results = cursorConnectionAndRead("SELECT text FROM greetings")

    bot.send_message(message.chat.id, results)

    # logging.debug('A debug message')
    # logging.info('Some information')
    # logging.warning('A shot across the bows')

    results = cursorConnectionAndRead("SELECT questionTEXT FROM First_4_questions")
    questioning(message)

def considiration(message):
    bot.send_message(message.chat.id,'"Статус вашей заявки: Ваша заявка на рассмотрении" ')
    bot.send_message(message.chat.id, 'для просмотра вашего статуса еще раз отправьте /start')

def userRights(message):
    bot.send_message(message.chat.id, "Ваш статус: Вы зарегистрированы как пользователь")

if __name__=='__main__':
    bot.polling(none_stop = True)


