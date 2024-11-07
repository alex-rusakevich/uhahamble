import random
from itertools import chain
from logging import getLogger
from typing import List

from uhahamble.utils.cache import cached

from .AnekdotRu import AnekdotRu
from .AnekdotyRu import AnekdotyRu
from .JokeWebsiteBase import JokeWebsiteBase
from .NewanekiRu import NewanekiRu

logger = getLogger(__name__)

JOKE_WEBSITES: List[JokeWebsiteBase] = [AnekdotRu(), AnekdotyRu(), NewanekiRu()]


@cached()
def get_joke_list() -> List[str]:
    jokes = [joke_website.get_jokes() for joke_website in JOKE_WEBSITES]

    return list(chain(*jokes))


def get_joke() -> str:
    return random.choice(get_joke_list())
