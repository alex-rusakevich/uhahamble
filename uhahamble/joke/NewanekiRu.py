import re
from logging import getLogger
from typing import List

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from uhahamble.utils.bs4 import innerHTML, strip_html

from .JokeWebsiteBase import JokeWebsiteBase

ua = UserAgent()
logger = getLogger(__name__)


class NewanekiRu(JokeWebsiteBase):
    NAME = "newaneki.ru"
    URL = "https://newaneki.ru/"

    def get_jokes(self) -> List[str]:
        results: List[str] = []

        page = requests.get("https://newaneki.ru/", headers={"User-Agent": ua.random})
        html = BeautifulSoup(page.text, "html.parser")

        for div_text in html.select("article.blog-entry div.blog-entry-summary p"):
            anec = innerHTML(div_text)

            if "<img" in anec:
                continue

            if "читать дальше" in anec:
                continue

            anec = anec.replace("<br>", "\n").replace("<br/>", "\n")
            anec = re.sub(r"\n{3,}", "\n\n", anec)
            anec = strip_html(anec)

            results.append(self.mark_joke(anec))

        return results
