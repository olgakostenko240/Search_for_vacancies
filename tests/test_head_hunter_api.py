from unittest.mock import patch

from src.head_hunter_api import HeadHunterAPI


@patch("src.head_hunter_api.requests.get")
def test_api_connect(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items": {"login": "test_user", "public_repos": 10}}
    expected_result = {"login": "test_user", "public_repos": 10}
    result = HeadHunterAPI().load_vacancies("test_user")
    assert result == expected_result
