import telebot
from telebot import types
import random
from config import token
import time

bot = telebot.TeleBot(token)


def roll_dice(message):
    rand = random.randint(1, 6)
    bot_rand = random.randint(1, 6)
    bot.send_message(message.chat.id, f'у тебя выпало {rand}')
    time.sleep(1)
    bot.send_message(message.chat.id, f'у меня выпало {bot_rand}')
    if rand > bot_rand:
        bot.send_message(message.chat.id, "Ты победил")
    elif rand == bot_rand:
        bot.send_message(message.chat.id, 'ничья')
    else:
        bot.send_message(message.chat.id, 'я победил')


@bot.message_handler(commands=['start'])
def command_help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    roll = types.KeyboardButton('⚾️ play')
    keyboard.add(roll)

    bot.send_message(message.chat.id, f"Welcome {message.from_user.first_name}", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    if message.text == '⚾️ play':
        roll_dice(message)

    else:
        bot.send_message(message.chat.id, '🧐')


bot.polling()
