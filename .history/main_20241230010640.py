from  transliterate import to_cyrillic, to_latin
import telebot

key = "8182193042:AAGphBVUX9ALWgTvCJ30VG8y20IpncsYd2Y"

bot = telebot.TeleBot(key, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    response = "Assalomu aleykum, "
    bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()





