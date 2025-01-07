from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """Родительский класс для get-запроса"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> Any:
        """Метод отправки get-запроса на сайт Head Hunter"""
        pass

    @abstractmethod
    def api_connect(self) -> Any:
        """Подключение к API hh.ru"""
        pass
