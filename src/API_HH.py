import requests
from abc import ABC, abstractmethod


class APIVacancies(ABC):
    """
    Абстрактный класс для работы по API с сервисами вакансий.
    """

    @abstractmethod
    def getting_vacancies(self, keyword):
        pass


class HeadHunterRuAPI(APIVacancies):
    """
    Подключается к API и получает вакансии по ключевому слову
    """

    def getting_vacancies(self, keyword):
        """
        Получает вакансии по ключевому слову из API сервиса HH.ru поиска вакансий
        param keyword: Ключевое слово для поиска вакансий
        per_page: 100 - Выводить 100 вакансий
        :return: JSON-данные с информацией о вакансиях
        """

        url = 'https://api.hh.ru/vacancies'
        params = {
            "text": keyword,
            "per_page": 100,
        }
        response = requests.get(url, params=params)
        return response.json()['items']

a = HeadHunterRuAPI()
b = 1
for vacance in a.getting_vacancies("Логист Екатеринбург"):
    print(b)
    b += 1
    print(vacance)
