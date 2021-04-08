import telebot
from telebot import types
import random
from config import token
import time

bot = telebot.TeleBot(token)
score = {}


def roll_dice(message):
    rand = random.randint(1, 6)
    bot_rand = random.randint(1, 6)
    winner = None
    bot.send_message(message.chat.id, f'у тебя выпало {rand}')
    time.sleep(1)
    bot.send_message(message.chat.id, f'у меня выпало {bot_rand}')
    if rand > bot_rand:
        bot.send_message(message.chat.id, "Ты победил")
        winner = 0
    elif rand == bot_rand:
        bot.send_message(message.chat.id, 'ничья')
        winner = None
    else:
        bot.send_message(message.chat.id, 'я победил')
        winner = 1
    return winner


@bot.message_handler(commands=['start'])
def command_help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    roll = types.KeyboardButton('⚾️ play')

    keyboard.add(roll, exit)

    bot.send_message(message.chat.id, f"Welcome {message.from_user.first_name}", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    if message.text == '⚾️ play':
        global score
        if message.from_user.id not in score:
            round = [0, 0]
            score[message.from_user.id] = round
        winner = roll_dice(message)
        if winner != None:
            score[message.from_user.id][winner] += 1
        bot.send_message(message.chat.id, f'счет {score[message.from_user.id][0]}:{score[message.from_user.id][1]} {message.from_user.id}')

    else:
        bot.send_message(message.chat.id, '🧐')


bot.polling()
