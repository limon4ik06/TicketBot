import re
from currency import currency
from datetime import datetime
import telebot
import requests
from telebot import types
curs = currency()
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
        bot.send_message(message.chat.id, f'Курс Доллара: {curs.curs_usd()} грн.')
    elif message.text == 'ЖД Билеты':
        res = bot.send_message(message.chat.id,'Введите дату: дд.мм.гггг')
        bot.register_next_step_handler(res, ticket)

def ticket(message):
    if re.search(r'\d{2}.\d{2}.\d{4}', message.text):
        try:
            datetime.strptime(message.text, '%d.%m.%Y')
        except ValueError:
            bot.send_message(message.chat.id, 'Введена неверная дата!!!')
            bot.send_message(message.chat.id, 'Введите правильную дату)')
        else:
            date = message.text
            markup_inline = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton(text='Киев', callback_data='kiyv')
            item2 = types.InlineKeyboardButton(text='Полтава', callback_data='poltava')
            item3 = types.InlineKeyboardButton(text='Славянск', callback_data='slavyansk')
            item4 = types.InlineKeyboardButton(text='Харьков', callback_data='charkov')
            markup_inline.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Откуда:', reply_markup=markup_inline)

@bot.callback_query_handler(func= lambda callback: callback.data)
def station_from(callback):
    if callback.data == 'kiyv':
        station1 = 'Киев'
    elif callback.data == 'poltava':
        station1 = 'Полтава'
    if station1 != None:
        markup_inline = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Киев', callback_data='kiyv')
        item2 = types.InlineKeyboardButton(text='Полтава', callback_data='poltava')
        item3 = types.InlineKeyboardButton(text='Славянск', callback_data='slavyansk')
        item4 = types.InlineKeyboardButton(text='Харьков', callback_data='charkov')
        markup_inline.add(item1, item2, item3, item4)
        bot.send_message(callback.message.chat.id, 'Куда:', reply_markup=markup_inline)
        if callback.data == 'poltava':
            station2 = 'Полтава'
            print(station2)
        if callback.data == 'kiyv':
            station2 = 'Киев'
            print(station2)
    if station2 != None:
        pass

bot.polling(none_stop=True, interval=0)
