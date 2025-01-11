from typing import Any


def top_vacancy(number: Any, my_list: Any) -> Any:
    """Функция вывода Топ-n вакансий для пользователя"""
    if number == "":
        return my_list
    else:
        return my_list[0: int(number)]


def filter_city(my_list: Any, words: str) -> list:
    """Метод фильтрации списка вакансий по нужному городу"""
    result_city = []
    for i in my_list:
        if words == i["city"]:  # or words == i["description"] or words == i["salary"]:
            result_city.append(i)
    return result_city
