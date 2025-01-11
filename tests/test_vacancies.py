from src.vacancies import Vacancy
from unittest.mock import patch


def test_vacancy_init(first_vacancy):
    assert first_vacancy.name == "врач"
    assert first_vacancy.city == "Москва"
    assert first_vacancy.salary == 70000
    assert first_vacancy.url == "https://hh.ru/employer/11405458"
    assert first_vacancy.description == "Высшее медицинское образование."


def test_vacancy_str(first_vacancy):
    assert str(first_vacancy) == "врач Москва 70000 https://hh.ru/employer/11405458 Высшее медицинское образование."


def test_vacancy_le(first_vacancy, first_vacancy_1):
    assert (first_vacancy <= first_vacancy_1) == True
    assert (first_vacancy_1 <= first_vacancy) == False


def test_vacancy_funct_dict(first_vacancy):
    assert first_vacancy.func_dict == {
        "name": "врач",
        "city": "Москва",
        "salary": 70000,
        "url": "https://hh.ru/employer/11405458",
        "description": "Высшее медицинское образование.",
    }


@patch("src.vacancies.Vacancy.processing_method")
@patch("src.head_hunter_api.HeadHunterAPI")
def test_processing_method(mock_vacancies, mock_processing_method):
    mock_vacancies.return_value = {"salary": {"from": 3000}}
    mock_processing_method.return_value = 3000
    expected_result = 3000
    result = Vacancy.processing_method("test_user")
    assert result == expected_result


@patch("src.vacancies.Vacancy.processing_method")
@patch("src.head_hunter_api.HeadHunterAPI")
def test_processing_method_1(mock_vacancies, mock_processing_method):
    mock_vacancies.return_value = {
        "name": "Врач",
        "area": {"name": "Москва"},
        "salary": {"from": 5000, "to": None, "currency": "RUR"},
        "alternate_url": "https://hh.ru/vacancy/115057777",
        "snippet": {"requirement": "Высшее медицинское образование."},
    }
    mock_processing_method.return_value = [
        {
            "name": "Врач",
            "city": "Москва",
            "salary": 5000,
            "url": "https://hh.ru/vacancy/115057777",
            "description": "Высшее медицинское образование.",
        }
    ]
    expected_result = [
        {
            "name": "Врач",
            "city": "Москва",
            "salary": 5000,
            "url": "https://hh.ru/vacancy/115057777",
            "description": "Высшее медицинское образование.",
        }
    ]
    result = Vacancy.processing_method('"test_user"')
    assert result == expected_result
