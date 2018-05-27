import telebot
import config
import requests

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types = ["text"])
def text_handler_1(message):
    city = message.text
    data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+'&APPID=c88c03e0d228641b89c36a1b48937bb7')
    bot.send_message(message.chat.id,int(data.json()['main']['temp_min']-273))
    print(int(data.json()['main']['temp_min']-273))

if __name__ == '__main__':
    bot.polling(none_stop = True)
