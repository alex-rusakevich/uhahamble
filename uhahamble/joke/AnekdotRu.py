import re
from logging import getLogger
from typing import List

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from uhahamble.utils.bs4 import innerHTML

from .JokeWebsiteBase import JokeWebsiteBase

ua = UserAgent()
logger = getLogger(__name__)


class AnekdotRu(JokeWebsiteBase):
    NAME = "anekdot.ru"
    URL = "https://www.anekdot.ru/"

    @staticmethod
    def get_jokes() -> List[str]:
        results: List[str] = []

        page = requests.get("https://www.anekdot.ru", headers={"User-Agent": ua.random})
        html = BeautifulSoup(page.text, "html.parser")

        for div_text in html.select("div.topicbox div.text"):
            anec = innerHTML(div_text).replace("<br>", "\n").replace("<br/>", "\n")
            anec = re.sub(r"\n{3,}", "\n\n", anec)

            if "читать дальше" in anec:
                continue

            results.append(anec)

        return results
