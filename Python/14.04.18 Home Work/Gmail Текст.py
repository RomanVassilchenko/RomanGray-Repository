import smtplib
import telebot
import config
import requests
bot = telebot.TeleBot(config.token)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Введите 5 пунктов: Вашу почту, Почту на которую хотите написать, Ваш пороль, Название email и текст')

start_command_handler = CommandHandler('start', startCommand)


@bot.message_handler(content_types = ["text"])
def text_handler_1(message):
    r = int(1)

    if(r == 5):
        body = message.text
        r += 1
        
    if(r == 4):
        msg['Subject'] = message.text
        r += 1
    
    if(r == 3):
        mypass = message.text
        r += 1
        
    if(r == 2):
        toaddr = message.text
        r += 1
        
    if(r == 1):
        fromaddr = message.text
        r += 1
    

    if(r == 6):         
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

         

        msg.attach(MIMEText(body, 'plain'))
         
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        

if __name__ == '__main__':
    bot.polling(none_stop = True)


    

