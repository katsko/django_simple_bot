from django.conf import settings
import telebot
from .models import Msg


bot = telebot.TeleBot(settings.TG_TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Send msg for add to db. After try /info')


@bot.message_handler(commands=['info'])
def info(message):
    count = Msg.objects.all().count()
    result = f'count: {count}'
    bot.reply_to(message, result)


@bot.message_handler(func=lambda message: True)
def get_msg(message):
    msg = Msg.objects.create(text=message.text)
    result = f'db msg id: {msg.id}'
    bot.reply_to(message, result)
