import multiprocessing
from logging import getLogger

import telebot

from .config import BOT_TOKEN

logger = getLogger()

bot_instance = telebot.TeleBot(
    BOT_TOKEN,
    skip_pending=True,
    parse_mode="MARKDOWN",
    threaded=True,
    num_threads=multiprocessing.cpu_count(),
    disable_web_page_preview=True,
)
