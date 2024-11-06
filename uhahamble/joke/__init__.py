import random
from itertools import chain
from logging import getLogger
from typing import List

from .AnekdotRu import AnekdotRu
from .JokeWebsiteBase import JokeWebsiteBase

logger = getLogger(__name__)

JOKE_WEBSITES: List[JokeWebsiteBase] = [AnekdotRu()]


def get_joke_list() -> List[str]:
    jokes = [joke_website.get_jokes() for joke_website in JOKE_WEBSITES]

    return list(chain(*jokes))


def get_joke() -> str:
    return random.choice(get_joke_list())
