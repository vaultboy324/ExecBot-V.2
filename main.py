import telebot

from entities.requests import Requests
from entities.user import User

import requests
from requests.auth import HTTPDigestAuth

import pyodata
from pyodata.v2.service import GetEntitySetFilter

from config import Config

bot = telebot.TeleBot(Config.TOKEN)

telebot.apihelper.proxy = {Config.PROXY_PROTOCOL : Config.PROXY_IP}

user_instance = User(0)
user_instance.set_uname("")
user_instance.set_initial_password()


@bot.message_handler(commands=['start'])
def send_welcome(message):
	user_instance.create_new_user(message.from_user.id)
	sap_user = Requests.get_user(user_instance)

	if not sap_user:
		bot.reply_to(message, "Введите ваш uname")
	else:
		user_instance.create_user_by_response(sap_user)
		bot.reply_to(message, f"Вы авторизованы под uname'ом {user_instance.get_uname()}\n"
		f"Ваш пароль: {user_instance.get_encode_password()}")

	print(sap_user)

	pass


@bot.message_handler(commands=['uname'])
def send_uname(message):
	user_instance.create_new_user(message.from_user.id)
	sap_user = Requests.get_user(user_instance)

	if Requests.check_user(user_instance):
		bot.reply_to(message, f"Ваш текущий uname: {sap_user[0][1]}. Для сброса используйте команду /reset")
	else:
		bot.reply_to(message, "Введите ваш uname")


@bot.message_handler(commands=['reset'])
def reset(message):
	user_instance.create_new_user(message.from_user.id)

	Requests.delete_user(user_instance)

	bot.reply_to(message, "Ваша авторизация была сброшена")

	pass


@bot.message_handler(commands=['status'])
def get_status(message):
	user_instance.create_new_user(message.from_user.id)
	if Requests.check_user(user_instance):
		SERVICE_URL = 'https://ts.execution.su/ts/index.html?sap-client=150&sap-language=RU#/Timesheet'
		session = requests.Session()
		session.auth = ("ASOLOBUTO", "test11")
		session.headers.update({
			'x-test': 'true'
		})
		#session.get(SERVICE_URL, headers={'x-test2': 'true'})
		client = pyodata.Client(SERVICE_URL, session)
		project_list = client.entity_sets.MyProjectListSet.get_enities().select("ProjText")
		for project in project_list:
			print(project)

		bot.reply_to(message, "На данный момент времени - это всё, что я могу(")
		return
	if not user_instance.get_uname():
		bot.reply_to(message, "у вас не задан uname. Введите uname")
		return
	if not user_instance.get_password():
		bot.reply_to(message, "у вас не задан пароль. Введите пароль")
		return


@bot.message_handler()
def parser(message):
	user_instance.create_new_user(message.from_user.id)
	if not user_instance.get_uname():
		user_instance.set_uname(message.text)

		bot.reply_to(message, "Ваш uname сохранён. Теперь настало время ввести пароль")

		return

	if not user_instance.get_password():
		user_instance.set_password(message.text)

		Requests.insert_user(user_instance)

		bot.reply_to(message, "Ваш пароль сохранён. Поздравляю! Вы теперь в системе(на самом деле нет, "
							  "это же ведь просто тест работы с БД)")

		return


bot.polling()