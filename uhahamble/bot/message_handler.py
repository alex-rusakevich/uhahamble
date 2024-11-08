from telebot.types import Message

from uhahamble.joke import JOKE_WEBSITES, get_joke

from .bot_instance import bot_instance as bot


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.reply_to(message, "Привет! Напиши мне /joke, и получишь анекдот")


@bot.message_handler(commands=["help"])
def send_help(message: Message):
    websites = [i.NAME for i in JOKE_WEBSITES]
    websites_str = ", ".join(websites[:-1]) + " и " + websites[-1]

    bot.reply_to(
        message,
        f"""
@uhahamble\\_bot — вашей бабушке зайдет

/joke — написать шутку

Спасибо авторам и администрации сайтов {websites_str}. Если вам понравились шутки из этих сайтов, \
не стесняйтесь их посетить! :D

Автор бота — @alerus\\_by

""".strip(),
        parse_mode="MARKDOWN",
    )


@bot.message_handler(commands=["joke"])
def send_joke(message: Message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, get_joke())
