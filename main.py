import telebot

TOKEN = "7480950291:AAEFiyrK_JvyE7EDEZSj9Ss7BpRRntFFI2o"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا بك في بوت المتجر!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
