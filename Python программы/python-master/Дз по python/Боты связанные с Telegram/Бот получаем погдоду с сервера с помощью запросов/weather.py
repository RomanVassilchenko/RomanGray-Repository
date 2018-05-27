import telebot
import config
import requests

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def text_handler_1(message):
    city = message.text
    data = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=58457cb0014568039f79584ed7dc67ca')
    bot.send_message(message.chat.id,int(data.json()['main']['temp_min']-273))
    print(int(data.json()['main']['temp_min']-273))



if __name__=='__main__':
    bot.polling(none_stop = True)
