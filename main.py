import os

from src.head_hunter_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.vacancy_json import HHVacancy
from src.utils import top_vacancy, filter_city
from config import PATH_HOME

path_to_file = os.path.join(PATH_HOME, "data", "vacancies.json")

def user_interaction():
    """Функция для взаимодействия с клиентом"""
    search_query = input("Введите интересующую вас вакансию: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите город в которм ищите данную вакансию: ")
    hh = HeadHunterAPI()
    result_hh = hh.load_vacancies(search_query)
    receiving_vacancies = Vacancy.processing_method(result_hh)
    filter_n = filter_city(receiving_vacancies, filter_words)
    result_top_n = top_vacancy(top_n, filter_n)
    return result_top_n


if __name__ == "__main__":
    result = user_interaction()
    print(result)

#Проверка работы программы полностью
if __name__ == "__main__":
    first = HeadHunterAPI()
    data = first.load_vacancies('python')
    result_f = first.vacancies
    print(result_f)
    result_vacancy = Vacancy("врач", "Москва", 80000, 'https://hh.ru/employer/11405458',
                             'Высшее медицинское образование.')
    print(result_vacancy.name)
    print(result_vacancy.city)
    print(result_vacancy.salary)
    print(result_vacancy.url)
    print(result_vacancy.description)
    result_vacancy1 = Vacancy("врач", "Санкт-Петербург", 70000, 'https://hh.ru/employer/11405459',
                              'Высшее медицинское образование.')
    print(result_vacancy1.name)
    print(result_vacancy1.city)
    print(result_vacancy1.salary)
    print(result_vacancy1.url)
    print(result_vacancy1.description)
    result_v = result_vacancy <= result_vacancy1
    print(result_v)
    result_d = result_vacancy.func_dict
    print(result_d)
    data_v = Vacancy.processing_method(result_f)
    print(data_v)
    result_w = filter_city(data_v, "Москва")
    print(result_w)
    data_t = top_vacancy(2, result_w)
    print(data_t)
    res_vacancy = HHVacancy(path_to_file)
    res_vac = res_vacancy.safe_vacancy(data_t)
    res_f = res_vacancy.vacancy_from_file('Python бэкенд разработчик')
    res_v = res_vacancy.delete_vacancy("Программист / разработчик (junior)")
    print(res_f)
