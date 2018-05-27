import config
import requests
import telebot
import json
from telebot import apihelper
from datetime import datetime
from telebot import types
import sqlite3
bot = telebot.TeleBot(config.token)
_db_Number_of_User = 0
_db_User_Status = 0
myArray =[_db_Number_of_User,_db_User_Status]
Complaints = [_db_Number_of_User,_db_User_Status]
print(myArray)
WaitMode = 0
UserMode = 1
AdminMode = 2
#write_To_Log(message.from_user.id, "user write")
def get_Time_Now():
    return datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")

def write_To_Log(mid, text):
    with open("log.txt", "a+", encoding='utf-8') as flog:
        flog.write(get_Time_Now()+" "+str(mid)+" "+text+"\n")

@bot.message_handler(commands = ['start'])
def start(message):
    try:
        res = cursorConnectR("SELECT Status FROM Answers WHERE Id =%s" %message.from_user.id)
        res =int(res[0][0])
        if res == 1:
            userRights(message)
            
        elif res == 0:
            considiration(message)
            
        elif res == 2:
            adminRights(message)
    except:
        main(message)
@bot.message_handler(commands =['info'])
def info(message):
    try:
        res = cursorConnectR(
            "SELECT Status FROM Answers WHERE Id =%s" % message.from_user.id)
        res = int(res[0][0])
        print(res)
        if res == 0:
            bot.send_message(message.chat.id,
                             'Ваша заявка пока что на рассмотрении, Ожидайте ')
            write_To_Log(message.from_user.id, "user write /info and status = 0")
        elif res == 1:
            bot.send_message(message.chat.id,
                             'Вы зарегестрированы как "Пользователь", отправьте повторно команду /start для начала работы')
            write_To_Log(message.from_user.id, "user write /info and status = user")
        elif res == 2:
            bot.send_message(message.chat.id,
                             'Вы зарегестрированы как "Админ", отправьте повторно команду /start для начала работы')
        write_To_Log(message.from_user.id, "user write /info and status = Admin")
    except:
        bot.send_message(message.chat.id,'Пока вы не зарегисрированы, отправьте повторно команду /start для регистрации')

@bot.message_handler(commands = ['admin'])
def adminActivate(message):
    bot.send_message(message.chat.id,"Вы ввели команду, чтобы стать Админом ")
    write_To_Log(message.from_user.id, "user write /admin")
    bot.send_message(message.chat.id,"Введите пароль:")
    bot.register_next_step_handler(message,adminPasswordCheck)

def main(message):
    global results
    global myArray

    myArray = list(myArray)
    myArray = [_db_Number_of_User, _db_User_Status]
    results = cursorConnectR("SELECT Text FROM TextForUser")
    bot.send_message(message.chat.id, results)
    results = cursorConnectR("SELECT Text FROM Questions")
    questioning(message)
    
def questioning(message):
    global results
    global myArray
    print(results)
    if results !=[]:
        for i in results:
            bot.send_message(message.chat.id,i)
            bot.register_next_step_handler(message,questoningStep2)
            del results[0]
            break
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        results = cursorConnectR("SELECT Text FROM name_buttons WHERE id = 1")
        keyboard.add(*[types.KeyboardButton(name) for name in["Отправить"]])
        bot.send_message(message.chat.id, "Если все данные верны нажмите 'Отправить', в противном случае введите повторно данные заново нажав на /start", reply_markup=keyboard)
        myArray[_db_Number_of_User]=message.from_user.id
        myArray = tuple(myArray)
        bot.register_next_step_handler(message,ConfirmationOfRegistration)


    
def questoningStep2(message):
    
    myArray.append(message.text)
    print(myArray)    
    questioning(message)


def cursorConnectR(sql):
    conn = sqlite3.connect('Bot.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    info = cursor.fetchall()
    conn.close()
    return info

def cursorConnectW(tableName,insertingTurpleWithValues):
    conn = sqlite3.connect('Bot.db')
    cursor = conn.cursor()
    cursor.execute("insert into %s values %s"%(tableName,insertingTurpleWithValues))
    conn.commit()
    conn.close()


def cursorConnectU(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue):
    conn = sqlite3.connect('Bot.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE %s SET %s = '%s'  WHERE %s = %s" %(tableName,columnText,textValue,columnForOrientation,columnForOrientationValue))
    conn.commit()
    conn.close()

def ConfirmationOfRegistration(message):
    global myArray

    if message.text == "Отправить":
        bot.send_message(message.chat.id,
                         'Хорошо! вы прошли регистрацию, ваша заявка находится на рассмотрении администрации')
        bot.send_message(message.chat.id,
                         'Используйте команду /info для того чтобы узнать ваш статус')
        cursorConnectW("Answers", myArray)
    else:
        start(message)

def considiration(message):
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT text_after_registration FROM RegistrationComplete WHERE tag = 'spirit'"))

def userRights(message):
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM Status WHERE Name = 'user'"))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["О проекте", "Отправить сообщение","Мои обращения","Обратная связь"]])
    bot.send_message(message.chat.id,
                     "Для выбора функции нажмите на кнопку",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message,UserButtonChoose)

def UserButtonChoose(message):

    if message.text == "О проекте":
        AboutProject(message)

    if message.text == "Отправить сообщение":
        SendMessage(message)

    if message.text == "Мои обращения":
        MyTreatment(message)

    if message.text == "Обратная связь":
        Feedback(message)

    if message.text == "Грязь и мусор":
        DirtAndTrash(message)
    if message.text == "Ямы":
        Pits(message)
    if message.text == "Неисправное освещение":
        DefenciveLightning(message)
    if message.text == "Показать все категории":
        ShowAllCategory(message)

def adminPasswordCheck(message):
    if  str(cursorConnectR("SELECT Text FROM AdminText WHERE Name = Password")[0][0]) == message.text :
        cursorConnectU("Answers","Status",AdminMode,"Id",message.from_user.id)
        bot.send_message(message.chat.id,"Теперь вы зарегистрированы как Администратор и можете все редактировать")
        write_To_Log(message.from_user.id, "user write Correct password")
    else:
        bot.send_message(message,"Пороль")
        write_To_Log(message.from_user.id, "user write Wrong password")


def adminRights(message):

    bot.send_message(message.chat.id,  cursorConnectR(
        "SELECT Text FROM Status WHERE Name = 'admin'"))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ["Ключевые слова", "Изменить 'Вопросы'","Редактировать текст","События","Участники группы","Вакансии" , "О проекте", "Стать пользователем"]])
    bot.send_message(message.chat.id,
                     "Для выбора функции нажмите на кнопку",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message,AdminButtonChoose)

def AdminButtonChoose(message):

    if message.text == "Ключевые слова":
        KeyWords(message)

    if message.text == "Изменить 'Вопросы'":
        ChangeQuestions(message)

    if message.text == "Редактировать текст":
        ChangeText(message)

    if message.text == "События":
        Developments(message)

    if message.text == "Участники группы":
        GroupMembers(message)

    if message.text == "Вакансии":
        Vacancies(message)
    if message.text == "О проекте":
        AdminAboutProject(message)
    if message.text == "Стать пользователем":
        BecomeUser(message)
def ChangeQuestions (message):
    global results
    global myArray

    bot.send_message(message.chat.id,'Вы выбрали функцию "Изменить Вопросы". Теперь вы можетe изменить текст, который бот отправляет пользователю после регистрации.'
                                     'Вам по очереди будет выведен текст каждого вопроса, если вы захотите изменить его то просто отпрвьте текст с новым вопросом')
    write_To_Log(message.from_user.id, "Admin " + message.from_user.username + " write Change Questions")
    results = cursorConnectR("SELECT Id FROM Questions")

    ChangeQuestions2(message)

def ChangeQuestions2(message):
    global i
    global results
    for i in results:
        print(cursorConnectR("SELECT Text FROM Questions WHERE Id=%s" % i))
        bot.send_message(message.chat.id,"Редактируемый вопрос" + "<"+str(cursorConnectR("SELECT Text FROM Questions WHERE Id=%s" %i)[0][0])+">")
        
        bot.register_next_step_handler(message,ChangeQuestions3)       
        del results[0]
        print (results)
        break

def ChangeQuestions3(message):
    global i
    try:
        i = i[0]
    except:
        print("'i' is already int")
    cursorConnectU("Questions", "Text", message.text, "Id", i)
    if results == []:
        bot.send_message(message.chat.id,"Вы поменяли текст вопросов при регистрациии")
        adminRights(message)
    write_To_Log(message.from_user.id, "Admin " + message.from_user.username + " change answer")
    ChangeQuestions2(message)

def KeyWords(message):
    print("ChangeQuestions")
    bot.send_message(message.chat.id,'Вы выбрали функцию "Ключевые слова". Теперь вы можете изменить содержимое вопросов при регистрации.'
                                     'Вам по очереди будет выведен текст каждого вопроса, если вы захотите изменить его то просто отпрвьте текст с новым вопросом')
    write_To_Log(message.from_user.id, "Admin write Keywords")
def ChangeText(message):
    print("Change Text")

def Developments(message):
    print("Developments")
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM TextForUser WHERE Id = 5"))
    bot.register_next_step_handler(message, UserButtonChoose)
def GroupMembers(message):
    print("Group Members")
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM TextForUser WHERE Id = 5"))
    bot.register_next_step_handler(message, UserButtonChoose)
def Vacancies(message):
    print("Vacancies")
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM TextForUser WHERE Id = 5"))
    bot.register_next_step_handler(message, UserButtonChoose)
def AboutProject(message):
    print("About Message")
    results = cursorConnectR("SELECT Text FROM TextForUser WHERE id = 2")
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='читать далее...', url='http://telegra.ph/Telegraph-EHto-05-19')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, results, reply_markup = markup)
    bot.register_next_step_handler(message, UserButtonChoose)

def AdminAboutProject(message):
    print("AdminAboutProject")
    bot.send_message(message.chat.id,"Изменяемый текст:")
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM TextForUser WHERE Id = 2"))
    bot.register_next_step_handler(message, AdminAboutProject2)

    
def AdminAboutProject2(message):
    print("AdminAboutProject")
    cursorConnectU("TextForUser","Text",message.text,"Id",2)
    bot.send_message(message.chat.id,"Текст изменен!")
    bot.register_next_step_handler(message, AdminButtonChoose)
    
def SendMessage(message):
    print("Send Message")
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM TextForUser WHERE Id = 4"))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   ["Грязь и мусор", "Ямы", "Неисправное освещение", "Показать все категории", "Поменять избранные категории"]])
    bot.send_message(message.chat.id,
                     "Для выбора функции нажмите на кнопку",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, UserButtonChoose)

def MyTreatment(message):
    print("My Treatment")

def Feedback(message):
    print("Feedback")
    results = cursorConnectR("SELECT Text FROM TextForUser WHERE id = 3")
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Обратная связь', url='http://telegra.ph/Telegraph-EHto-05-19')
    # Изменить ссылку на обратную связь
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, results, reply_markup = markup)
def DirtAndTrash(message):
    print("DirtAndTrash")
    global Complaints
    Complaints = list(Complaints)
    print(Complaints)
    Complaints.clear()
    Complaints.append(message.chat.id)
    Complaints.append("Грязь и мусор")
    bot.send_message(message.chat.id,
                     "Введите адрес")
    bot.register_next_step_handler(message, RegisterAdress)

def Pits(message):
    print("Pits")
    global Complaints
    Complaints = list(Complaints)
    Complaints.append(message.chat.id)
    Complaints.append("Ямы")
    bot.send_message(message.chat.id,
                     "Введите адрес")
    bot.register_next_step_handler(message, RegisterAdress)


def DefectiveLighting(message):
    print("DefectiveLighting")
    global Complaints
    Complaints = list(Complaints)
    Complaints.append(message.chat.id)
    Complaints.append("Неисправное освещение")
    bot.send_message(message.chat.id,
                     "Введите адрес")
    bot.register_next_step_handler(message, RegisterAdress)


def RegisterAdress(message):
    global  Complaints
    Complaints = list(Complaints)
    Complaints.append(message.text)
    # Добавить фото
    Complaints.append(1)
    bot.send_message(message.chat.id,
                     "Напишите комментарий")
    bot.register_next_step_handler(message, RegisterComments)

def RegisterComments(message):
    global Complaints
    Complaints = list(Complaints)
    Complaints.append(message.text)
    Complaints.append(0)
    Complaints = tuple(Complaints)
    cursorConnectW("Complaints", Complaints)

def ShowAllCategory(message):
    bot.send_message(message.chat.id, cursorConnectR(
        "SELECT Text FROM Category"))
def BecomeUser(message):
    print("Стать пользователем")
    cursorConnectU("Answers","Status",1,"Id",message.chat.id)
    bot.send_message(message.chat.id, "Вы стали пользователем! Чтобы начать напишите /start")

if __name__=='__main__':
    bot.polling(none_stop = True)

	
