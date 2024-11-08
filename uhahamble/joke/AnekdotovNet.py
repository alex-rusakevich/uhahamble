from logging import getLogger
from typing import List

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from uhahamble.utils.bs4 import innerHTML

from .JokeWebsiteBase import JokeWebsiteBase

ua = UserAgent()
logger = getLogger(__name__)


class AnekdotovNet(JokeWebsiteBase):
    NAME = "anekdotov.net"
    URL = "https://anekdotov.net/anekdot/"

    def get_jokes(self) -> List[str]:
        results: List[str] = []

        page = requests.get(
            "https://anekdotov.net/anekdot/", headers={"User-Agent": ua.random}
        )
        html = BeautifulSoup(page.text, "html.parser")

        for div_text in html.select("div.anekdot"):
            anec = innerHTML(div_text)

            if "<img" in anec:
                continue

            if "читать дальше" in anec:
                continue

            results.append(self.mark_joke(self.process_joke_html(anec)))

        return results
