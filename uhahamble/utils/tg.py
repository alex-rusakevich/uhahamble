from typing import List

from telebot.types import Message


def get_command_args(message: Message) -> List[str]:
    return message.text.split()[1:]
