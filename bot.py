import telebot
from telebot import types
import random

bot = telebot.TeleBot("YOUR TOKEN")

@bot.message_handler(commands=['furpic'])
def send_welcome(message):
	with open ('pic.txt', 'r') as file:
		lines = file.readlines()
		URL = random.choice(lines)
	bot.reply_to(message, URL)

@bot.message_handler(commands=['furgif'])
def send_welcome(message):
	with open ('gif.txt', 'r') as file:
		lines = file.readlines()
		URL = random.choice(lines)
	bot.reply_to(message, URL)

@bot.message_handler(commands=['ping'])
def send_welcome(message):
	bot.reply_to(message, "Понг!")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.chat.id	
	markup = types.ReplyKeyboardMarkup()
	itembtn1 = types.KeyboardButton('/furpic')
	itembtn2 = types.KeyboardButton('/furgif')
	markup.add(itembtn1, itembtn2)
	bot.send_message(chat_id, "Что отослать?", reply_markup=markup)

bot.polling()
