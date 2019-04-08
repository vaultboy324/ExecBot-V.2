import telebot
import psycopg2

from config import Config
from config import DatabaseConfig

from User import User
from Requests import Requests


bot = telebot.TeleBot(Config.TOKEN)

telebot.apihelper.proxy = {Config.PROXY_PROTOCOL : Config.PROXY_IP}

conn = psycopg2.connect(dbname=DatabaseConfig.DATABASE, user=DatabaseConfig.USER,
							password=DatabaseConfig.PASSWORD, host=DatabaseConfig.HOST)
cursor = conn.cursor()


def connect():
	conn = psycopg2.connect(dbname=DatabaseConfig.DATABASE, user=DatabaseConfig.USER,
							password=DatabaseConfig.PASSWORD, host=DatabaseConfig.HOST)
	cursor = conn.cursor()


def disconnect():
	cursor.close()
	conn.close()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здорова")


@bot.message_handler(commands=['users'])
def send_user_list(message):
	connect()
	new_user = User(1, 'ASOLOBUTO00', 'test11')
	result = Requests.get_user_by_logpass(new_user, cursor)
	print(result)
	disconnect()
	bot.reply_to(message, "Прочитано")


bot.polling()