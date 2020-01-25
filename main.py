import telebot

# from telebot import apihelper

# Через proxy
# apihelper.proxy = {
#     'http': 'http://117.1.16.131:8080',
#     'https': 'http://117.1.16.131:8080',
# }

bot = telebot.TeleBot("990218336:AAGFZuiu47SrZQF5CGBoF7VaEjn8n5HxFMU")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Приветствие")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Тут будет помощь")


@bot.message_handler(commands=['newcategory'])
def send_welcome(message):
    bot.reply_to(message, "создана")


@bot.message_handler(commands=['add'])
def send_welcome(message):
    bot.reply_to(message, "добавлено")


@bot.message_handler(commands=['delcategory'])
def send_welcome(message):
    # TODO: подтверждение добавления
    bot.reply_to(message, "удалено")


@bot.message_handler(commands=['delelement'])
def send_welcome(message):
    # TODO: подтверждение добавления
    bot.reply_to(message, "элемент удален")


@bot.message_handler(content_types=["text"])
def send_welcome(message):
    # Вводим название категории, а он нам возвращает случайное значение
    bot.reply_to(message, "случайный элемент")

bot.polling()
