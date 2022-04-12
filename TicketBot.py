import sys, simplejson as json
import requests
from datetime import datetime
import telebot
from telebot import types
import time
import mysql.connector
from bs4 import BeautifulSoup
bot = telebot.TeleBot('5179481610:AAGCstlyt-zsBDWLjJlrMrPAytjLQVYJS7A')


def input_data(bot_message):
    bot_token = '5179481610:AAGCstlyt-zsBDWLjJlrMrPAytjLQVYJS7A'
    chat_id = ['948971487', '102737883']
    for id in chat_id:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + bot_message
        requests.get(send_text)


# input_data(me)


@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Курс")
    item2 = types.KeyboardButton("ЖД Билеты")
    markup.add(item1, item2)
    bot.send_message(m.chat.id, 'Hello, click on any Button', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == 'Курс':
        url = 'https://minfin.com.ua/currency/banks/usd/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        info = soup.find('div', class_='mfm-grey-bg').find('td', class_='responsive-hide mfm-text-left mfm-pl0').text
        bot.send_message(message.chat.id, f'Курс Доллара: {info} грн.')
    elif message.text == 'ЖД Билеты':
        bot.send_message(message.chat.id, 'Введите дату: дд.мм.гггг')
    elif message.text.find('%d.%d.%d'):
        try:
            datetime.strptime(message.text, '%d.%m.%Y')
        except ValueError:
            bot.send_message(message.chat.id, 'Введена неверная дата!!!')
        else:
            date = message.text
            bot.send_message(message.chat.id, date)



bot.polling(none_stop=True, interval=0)
