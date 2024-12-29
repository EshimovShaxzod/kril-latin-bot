from transliterate import to_cyrillic, to_latin
import telebot
import os


bot = telebot.TeleBot(os.getenv(""), parse_mode='HTML')

# Matnni kirill yoki lotin formatiga o‘tkazish
def transliterate_text(text):
    return to_cyrillic(text) if text.isascii() else to_latin(text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu aleykum, Xush kelibsiz!\nMatn kiriting")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    translated_text = transliterate_text(message.text)
    bot.reply_to(message, translated_text)

bot.polling()
