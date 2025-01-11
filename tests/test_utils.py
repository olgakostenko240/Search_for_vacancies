from src.utils import top_vacancy, filter_city


def test_top_vacancy(user_number):
    result = top_vacancy(1, user_number)
    assert result == [
        {
            "name": "Middle Python Developer",
            "city": "Санкт-Петербург",
            "salary": 160000,
            "url": "https://hh.ru/vacancy/115066149",
            "description": "Необходимо знание асинхронного программирования.",
        }
    ]


def test_filter_city(user_number):
    result = filter_city(user_number, "Москва")
    assert result == [
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


def test_filter_city_1(user_number):
    result = filter_city(user_number, "Казань")
    assert result == []
