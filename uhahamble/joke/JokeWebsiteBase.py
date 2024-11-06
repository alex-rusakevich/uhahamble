from typing import List


class JokeWebsiteBase:
    NAME: str
    URL: str

    def mark_joke(self, joke: str) -> str:
        return joke + f"\n\nИсточник: [{self.NAME}]({self.URL})"

    def get_jokes(self) -> List[str]:
        return []
