import telebot
from config import Config

bot = telebot.TeleBot(Config.TOKEN)

telebot.apihelper.proxy = {Config.PROXY_PROTOCOL : Config.PROXY_IP}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здорова")

bot.polling()