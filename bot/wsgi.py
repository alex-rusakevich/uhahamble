import os
import time
from logging import getLogger

import flask
import telebot
from flask import Flask, redirect, request

from bot.bot_instance import bot_instance as bot
from bot.config import BOT_TOKEN, DEBUG

logger = getLogger()


WEBHOOK_URL_BASE = os.environ.get("OUTER_URL", "127.0.0.1")
WEBHOOK_URL_PATH = "/{}/".format(BOT_TOKEN)


app = Flask(__name__)
app.logger = logger


@app.route(WEBHOOK_URL_PATH, methods=["POST"])
def get_message():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)


@app.route("/")
def root_hook():
    return redirect("https://t.me/uhahamble_bot", 302)


app.debug = DEBUG

bot.remove_webhook()
time.sleep(1)

bot.set_webhook(
    url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
    drop_pending_updates=True,
)

logger.info("Running in production mode: " + str(not app.debug))

# Starting waitress
wsgi_app = app.wsgi_app
