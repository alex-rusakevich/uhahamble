from bot.bot_instance import bot_instance as bot


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши мне `/joke`, и получишь анекдот")


@bot.message_handler(commands=["joke"])
def send_joke(message):
    bot.reply_to(message, "Ржака)")
