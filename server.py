#!/usr/bin/env python3

import os
import signal
import sys
import time
from logging import getLogger

from waitress import serve

from bot.bot_instance import bot_instance as bot
from bot.config import DEBUG

logger = getLogger(__name__)


def main():
    if len(sys.argv) == 1:
        raise Exception("Not enough arguments to run, stopping")

    command = sys.argv[1]

    if command == "prod":
        from bot.wsgi import wsgi_app

        waitress_args = {"port": os.environ.get("PORT", 8080)}
        serve(wsgi_app, **waitress_args)
    elif command == "dev":
        signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on Ctrl-C

        logger.info("Starting the bot...")
        bot.remove_webhook()
        time.sleep(1)

        logger.info("Running in polling mode...")
        bot.infinity_polling(
            restart_on_change=DEBUG,
            path_to_watch=os.path.join(".", "bot"),
        )

        logger.info("The bot has stopped.")
    else:
        raise Exception(f"Wrong command error: '{command}'. It must be 'prod' or 'dev'")


if __name__ == "__main__":
    main()
