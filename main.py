import telebot

from entities.requests import Requests
from entities.user import User

from config import Config

bot = telebot.TeleBot(Config.TOKEN)

telebot.apihelper.proxy = {Config.PROXY_PROTOCOL : Config.PROXY_IP}


@bot.message_handler(commands=['start'])
def send_welcome(message):
	user = User(message.from_user.id)
	sap_user = Requests.get_user(user)

	if not sap_user:
		Requests.insert_user(user)

	print(sap_user)

	pass


bot.polling()