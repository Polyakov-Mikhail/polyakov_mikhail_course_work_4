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
        area: 3 - Город поиска "Екатеринбург"
        per_page: 100 - Выводить 100 вакансий
        :return: JSON-данные с информацией о вакансиях
        """

        url = 'https://api.hh.ru/vacancies'
        params = {
            "text": keyword,
            "area": 3,
            "per_page": 100,
        }
        response = requests.get(url, params=params)
        return response.json()['items']
