from abc import ABCMeta, abstractmethod
from typing import List


class JokeWebsiteBase(metaclass=ABCMeta):
    NAME: str
    URL: str

    @staticmethod
    @abstractmethod
    def get_jokes() -> List[str]:
        return []
