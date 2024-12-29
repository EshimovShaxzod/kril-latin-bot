from  transliterate import to_cyrillic, to_latin
import telebot

key = "8182193042:AAGphBVUX9ALWgTvCJ30VG8y20IpncsYd2Y"

bot = telebot.TeleBot(key, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    response = "Assalomu aleykum, Xush kelibsiz!"
    response += "\nMatn kiriting"
    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    res = message.text
    if res.ascii():
        text = to_cyrillic(res)    
    else:
        text = to_latin(res)
    bot.reply_to(message,text)


bot.polling()




