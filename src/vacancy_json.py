import json
import os

from config import PATH_HOME
from src.basis_json_vacancis import JSONVacancy
from typing import Any

# Путь до файла log
path_to_file = os.path.join(PATH_HOME, "data", "vacancies.json")


class HHVacancy(JSONVacancy):
    """Класс для чтения и удаления файлов с данными по вакансиям из сайта HH.ru"""

    def __init__(self, file_name_save: str = path_to_file) -> None:
        """Инициализатор класса"""
        self.__file_name_save = file_name_save

    def get_file_name(self) -> str:
        """Метод для доступа к файлу"""
        return self.__file_name_save

    def safe_vacancy(self, stock_list: Any) -> str:
        """Метод для сохранения данных о вакансиях в файл"""
        if stock_list is None:
            return "Вакансий с такими критериями не найдено"
        elif stock_list is not None:
            if os.path.exists(self.get_file_name()):
                with open(self.get_file_name(), "r", encoding="utf-8") as file:
                    data_w = json.load(file)
                for i in stock_list:
                    if i not in data_w:
                        data_w.append(i)
                with open(self.get_file_name(), "w", encoding="utf-8") as file:
                    json.dump(data_w, file, indent=4, ensure_ascii=False)
            else:
                with open(self.get_file_name(), "w", encoding="utf-8") as file:
                    json.dump(stock_list, file, indent=4, ensure_ascii=False)

    def vacancy_from_file(self, words_sample: Any) -> list | str:
        """Метод для выборки нужных данных из файла"""
        result_data = []
        if os.path.exists(self.get_file_name()):
            with open(self.get_file_name(), "r", encoding="utf-8") as file:
                data_f = json.load(file)
            for i in data_f:
                if words_sample == i["name"]: #in i["description"] or words_sample == i["name"] or words_sample == i["city"]:
                    result_data.append(i)
            return result_data
        else:
            return "Файла с таким название не существует"

    def delete_vacancy(self, words_del: Any) -> str:
        """Метод для удаления не нужных данных из файла"""
        data_1 = []
        if os.path.exists(path_to_file):
            with open(self.get_file_name(), "r", encoding="utf-8") as file:
                data_z = json.load(file)
            for i in data_z:
                if words_del != i["city"] and words_del not in i["name"] and words_del not in i["description"]:
                    data_1.append(i)
            with open(self.get_file_name(), "w", encoding="utf-8") as file:
                json.dump(data_1, file, indent=4, ensure_ascii=False)
        else:
            return "Файла с таким название не существует"
