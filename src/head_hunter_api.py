import requests
from typing import Any
from src.parser import Parser


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Магический метод инициализаций объектов для отправки get-запроса"""
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: dict[str, str] = {"User-Agent": "HH-User-Agent"}
        self.__params: dict[str, int | str] = {"text": "", "per_page": 100}
        self.__vacancies: list = []

    def __api_connect(self) -> Any:
        """Подключение к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        print("Ошибка получения данных")

    @property
    def api_connect(self) -> Any:
        """Метод содания атрибута"""
        return self.__api_connect()

    def load_vacancies(self, keyword: str) -> Any:
        """Метод отправки get-запроса на сайт Head Hunter"""
        self.__params["text"] = keyword
        response = self.api_connect
        vacancies = response.json()["items"]
        self.__vacancies.extend(vacancies)
        return vacancies

    @property
    def vacancies(self) -> list:
        """Метод для получения данных"""
        return self.__vacancies
