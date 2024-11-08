import re
from typing import List

from uhahamble.utils.bs4 import strip_html


class JokeWebsiteBase:
    NAME: str
    URL: str

    def mark_joke(self, joke: str) -> str:
        return joke + f"\n\nИсточник: [{self.NAME}]({self.URL})"

    def process_joke_html(self, joke_html: str) -> str:
        anec = joke_html.replace("<br>", "\n").replace("<br/>", "\n")
        anec = re.sub(r"\n{3,}", "\n\n", anec)
        anec = strip_html(anec)

        return anec.strip()

    def get_jokes(self) -> List[str]:
        return []
