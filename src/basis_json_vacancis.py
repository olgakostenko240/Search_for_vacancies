from abc import ABC, abstractmethod
from typing import Any


class JSONVacancy(ABC):
    """Абстрактный метод для создания и удаления JSON-файлов"""

    @abstractmethod
    def safe_vacancy(self, stock_list: Any) -> str:
        """Метод для сохранения данных о вакансиях в файл"""
        pass

    @abstractmethod
    def vacancy_from_file(self, words_sample: Any) -> list | str:
        """Метод для выборки нужных данных из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self, words_del: Any) -> str:
        """Метод для удаления не нужного файла"""
        pass
