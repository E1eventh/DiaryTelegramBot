from telebot import apihelper, TeleBot
import string

apihelper.proxy = {'https':'socks5://178.197.248.213:1080'}

TOKEN = '880610183:AAF4k1WZWQ7_MyL7f5Guiqmn_ArDmkfBCK8'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот-ежедневник!')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower().find('привет') + 1 or message.text.lower().find('доброе утро') + 1 \
            or message.text.lower().find('добрый день') + 1 or message.text.lower().find('добрый вечер') + 1:
        bot.send_message(message.chat.id, 'Приветствую вас')
    elif message.text.lower().find('что ты умеешь') + 1 or message.text.lower().find('возможности') + 1 \
            or message.text.lower().find('возможностях') + 1:
        bot.send_message(message.chat.id, 'Я могу напоминать вам о важных событиях, о которых вы сообщите мне')
    else:
        bot.send_message(message.chat.id, 'Я не очень умный бот и многое не понимаю. Простите')

bot.polling(none_stop = True, timeout = 123)
