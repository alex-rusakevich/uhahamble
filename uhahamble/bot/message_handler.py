from telebot.types import Message

from uhahamble.joke import get_joke

from .bot_instance import bot_instance as bot


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.reply_to(message, "Привет! Напиши мне `/joke`, и получишь анекдот")


@bot.message_handler(commands=["joke"])
def send_joke(message: Message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, get_joke())
