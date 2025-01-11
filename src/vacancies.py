class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "city", "salary", "url", "description")

    def __init__(self, name: str, city: str, salary: int, url: str, description: str) -> None:
        """Метод иницилизации объекта"""
        self.name: str = name
        self.city: str = city
        self.salary: int = salary
        self.url: str = url
        self.description: str = description

    def __str__(self) -> str:
        """Магический метод для отображения информации об объекте класса"""
        return f"{self.name} {self.city} {self.salary} {self.url} {self.description}"

    @property
    def func_dict(self) -> dict[str, str | int]:
        """метод преобразования в словарь"""
        vacancy_dict = dict(
            name=self.name, city=self.city, salary=self.salary, url=self.url, description=self.description
        )
        return vacancy_dict

    def __le__(self, other) -> bool:
        """Метод сравнения вакансий между собой по зарплате"""
        if self.salary <= other.salary:
            return True
        else:
            return False

    @staticmethod
    def processing_method(data_vac) -> list:
        """Метод для обработки JSON-ответа от сайта HH.ru"""
        result = []
        for i in data_vac:
            if i["salary"]:
                if i["salary"]["currency"] == "RUR":
                    if i["salary"]["from"]:
                        salary = int(i["salary"]["from"])
                    else:
                        salary = 0
                else:
                    continue
                result.append(
                    {
                        "name": i["name"],
                        "city": i["area"]["name"],
                        "salary": salary,
                        "url": i["alternate_url"],
                        "description": i["snippet"]["requirement"],
                    }
                )
        return result
