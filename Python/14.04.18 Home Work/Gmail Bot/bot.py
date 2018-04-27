import telebot
import config
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types = ["text"])
def text_handler_1(message):
    words = message.text
    words.split() 
    fromaddr = words[0]
    toaddr = words[1]
    mypass = words[2]
    fromaddr = words[3]
    msg['Subject'] = words[4]
    body = words[5]
    
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

 
