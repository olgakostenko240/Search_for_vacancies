import pytest

from src.vacancies import Vacancy


@pytest.fixture
def first_vacancy():
    return Vacancy(
        name="врач",
        city="Москва",
        salary=70000,
        url="https://hh.ru/employer/11405458",
        description="Высшее медицинское образование.",
    )


@pytest.fixture
def first_vacancy_1():
    return Vacancy(
        name="врач",
        city="Санкт-Петербург",
        salary=80000,
        url="https://hh.ru/employer/11405459",
        description="Высшее медицинское образование.",
    )


@pytest.fixture
def user_number():
    return [
        {
            "name": "Middle Python Developer",
            "city": "Санкт-Петербург",
            "salary": 160000,
            "url": "https://hh.ru/vacancy/115066149",
            "description": "Необходимо знание асинхронного программирования.",
        },
        {
            "name": "Backend Python разработчик",
            "city": "Москва",
            "salary": 160000,
            "url": "https://hh.ru/vacancy/115069669",
            "description": "Опыт работы с PostgreSQL.",
        },
        {
            "name": "Программист / разработчик (junior)",
            "city": "Москва",
            "salary": 70000,
            "url": "https://hh.ru/vacancy/114928083",
            "description": "Есть подтверждённые учебные или пет-проекты.",
        },
    ]
