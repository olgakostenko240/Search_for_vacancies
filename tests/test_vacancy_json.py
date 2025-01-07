from unittest.mock import patch
from src.vacancy_json import HHVacancy


@patch("src.utils.top_vacancy")
def test_safe_vacancy(mock_top_vacancy):
    mock_top_vacancy.return_value = {"login": "user1", "public_repos": 2}
    expected_result = {"login": "user1", "public_repos": 2}
    result = HHVacancy().safe_vacancy(expected_result)
    assert result is None


@patch("src.vacancy_json.HHVacancy.vacancy_from_file")
def test_vacancy_from_file(mock_vacancy_from_file):
    mock_vacancy_from_file.return_value = {"login": "user1", "public_repos": 2}
    expected_result = {"login": "user1", "public_repos": 2}
    result = HHVacancy().vacancy_from_file("user_test")
    assert result == expected_result
