import telebot
from telebot import types
import random

bot = telebot.TeleBot("YOUR TOKEN")

@bot.message_handler(commands=['furpic'])
def send_furpic(message):
	with open ('pic.txt', 'r') as file:
		lines = file.readlines()
		URL = random.choice(lines)
	bot.send_photo(message.chat.id, URL)

@bot.message_handler(commands=['furgif'])
def send_furgif(message):
	with open ('gif.txt', 'r') as file:
		lines = file.readlines()
		URL = random.choice(lines)
	bot.send_document(message.chat.id, URL)

@bot.message_handler(commands=['ping'])
def send_ping(message):
	bot.send_message(message.chat.id, "Понг!")

@bot.message_handler(commands=['start'])
def send_markup(message):
	chat_id = message.chat.id	
	markup = types.ReplyKeyboardMarkup(True, False)
	markup.row('/furpic', '/furgif')
	bot.send_message(chat_id, "Что отослать?", reply_markup=markup)

bot.polling()
