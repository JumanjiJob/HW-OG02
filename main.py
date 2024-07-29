import telebot
from telebot import types
import datetime
import time
import threading
import random

bot = telebot.TeleBot('YOUR TOKEN')
def easy_level():
    new_list = []
    list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    list3 = ['!','@','#',"$",'%','&']
    while len(new_list) != 3:
        new_list.append(random.choice(list1))
    while len(new_list) != 6:
        new_list.append(random.choice(list2))
    while len(new_list) != 8:
        new_list.append(random.choice(list3))
        random.shuffle(new_list)
        word = ''.join(new_list)
    return word

def hard_level():
    new_list = []
    list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    list3 = ['!','@','#',"$",'%','&']
    while len(new_list) != 4:
        new_list.append(random.choice(list1))
    while len(new_list) != 8:
        new_list.append(random.choice(list2))
    while len(new_list) != 12:
        new_list.append(random.choice(list3))
        random.shuffle(new_list)
        word = ''.join(new_list)
    return word


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем онлайн-клавиатуру
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки
    btn1 = types.InlineKeyboardButton(text='Простой - 8 символов', callback_data='button1')
    btn2 = types.InlineKeyboardButton(text='Сложный - 12 символов', callback_data='button2')


    # Добавляем кнопки в клавиатуру
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, easy_level())
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, hard_level())

def send_reminders(chat_id):
    first_rem = '15:00'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem:
            bot.send_message(chat_id, "Не желаете обновить пароли?")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)
