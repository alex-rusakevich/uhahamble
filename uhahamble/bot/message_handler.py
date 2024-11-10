import random

from telebot.types import Message

from uhahamble.joke import JOKE_WEBSITES, get_joke, get_joke_list
from uhahamble.utils.tg import get_command_args

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
/joke 3 - написать 3 шутки. Число может быть любым от 1 до 5 включительно

Спасибо авторам и администрации сайтов {websites_str}. Если вам понравились шутки из этих сайтов, \
не стесняйтесь их посетить! :D

Автор бота — @alerus\\_by

""".strip(),
        parse_mode="MARKDOWN",
    )


@bot.message_handler(commands=["joke"])
def send_joke(message: Message):
    bot.send_chat_action(message.chat.id, "typing")

    args = get_command_args(message)

    if len(args) == 0:
        bot.reply_to(message, get_joke())
    elif len(args) == 1:
        jokes_num_str = args[0]

        if not jokes_num_str.isdigit():
            bot.reply_to(message, "🔴 Ошибка: аргумент команды должен быть числом")
            return

        jokes_num = int(jokes_num_str)

        if jokes_num < 1 or jokes_num > 5:
            bot.reply_to(
                message,
                "🔴 Ошибка: аргумент должен быть числом не меньше 1 и не больше 5",
            )
            return

        joke_list = get_joke_list()
        random.shuffle(joke_list)

        bot.reply_to(message, joke_list[0])

        for i in range(1, jokes_num):
            bot.send_message(message.chat.id, joke_list[i])
    else:
        bot.reply_to(message, "🔴 Ошибка: слишком много аргументов")
        return
