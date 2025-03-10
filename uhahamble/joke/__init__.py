import random
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from logging import getLogger
from typing import List

from uhahamble.bot.config import THREADS_COUNT
from uhahamble.utils.cache import cached

from .AnekdotovNet import AnekdotovNet
from .AnekdotRu import AnekdotRu
from .AnekdotovmirRu import AnekdotovmirRu
from .AnekdotyRu import AnekdotyRu
from .JokeWebsiteBase import JokeWebsiteBase
from .NekdoRu import NekdoRu
from .NewanekiRu import NewanekiRu

logger = getLogger(__name__)

JOKE_WEBSITES: List[JokeWebsiteBase] = [
    AnekdotRu(),
    AnekdotyRu(),
    NewanekiRu(),
    AnekdotovNet(),
    NekdoRu(),
    AnekdotovmirRu()
]


@cached(ttl_sec=60 * 60 * 1)  # One hour
def get_joke_list() -> List[str]:
    executor = ThreadPoolExecutor(max_workers=THREADS_COUNT)

    jokes = []

    for result in executor.map(
        lambda joke_website: joke_website.get_jokes(), JOKE_WEBSITES
    ):
        jokes.append(result)

    jokes = list(chain(*jokes))
    random.shuffle(jokes)

    return jokes


def get_joke() -> str:
    return random.choice(get_joke_list())
