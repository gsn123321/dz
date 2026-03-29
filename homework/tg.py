import telebot

TOKEN = "8244508279:AAEEbEn4RQdFYWuDx8PDYb5MIle3rMh2PtQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот 🤖")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()



