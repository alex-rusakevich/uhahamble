import os
import signal
import time
from logging import getLogger

import redis
from invoke import task
from waitress import serve

from uhahamble.bot.bot_instance import bot_instance as bot
from uhahamble.bot.config import DEBUG, OUTER_URL, REDIS_PREFIX

logger = getLogger(__name__)

getLogger("invoke").disabled = True


@task
def dev(c):
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on Ctrl-C
    getLogger("watchdog.observers.inotify_buffer").disabled = True

    logger.info("Starting the bot...")
    bot.remove_webhook()
    time.sleep(1)

    logger.info("Running in polling mode...")
    bot.infinity_polling(
        restart_on_change=DEBUG,
        path_to_watch=os.path.join(".", "uhahamble"),
    )

    logger.info("The bot has stopped.")


@task
def prod(c):
    from uhahamble.bot.wsgi import wsgi_app

    logger.info("Starting the bot...")
    bot.remove_webhook()
    time.sleep(1)

    waitress_args = {"port": os.environ.get("PORT", 8080)}
    serve(wsgi_app, kw=waitress_args)


@task
def clear_cache(c):
    r = redis.StrictRedis()

    for key in r.scan_iter(f"{REDIS_PREFIX}:*"):
        r.delete(key)


@task
def restart(c):
    c.run("touch tmp/restart.txt")
    c.run("sleep 3")
    c.run(f"curl {OUTER_URL} 2>&1")


@task
def mypy(c):
    c.run("mypy uhahamble", pty=True)
