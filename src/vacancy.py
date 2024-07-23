import json
# from typing import List, Optional
from src.API_HH import HeadHunterRuAPI


class Vacancy:
    """ Класс для работы с вакансиями """
    def __init__(self, name, salary, currency, url, description, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.url = url
        self.description = description
        self.requirement = requirement

    def __repr__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary} {self.currency}\n'
                f'Описание вакансии: {self.description}\n'
                f'Требования: {self.requirement}\n'
                f'Ссылка на вакансию: <{self.url}>\n')

    def __lt__(self, other):
        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary["from"] != 0 and other.salary["to"] != 0:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __str__(self):
        """Метод для представляния вакансий при печати"""
        return (f'{self.name}\n'
                f'{self.url}\n'
                f'{self.description}\n'
                f'{self.salary["from"] if self.salary["from"] == 0 else "ЗП от не указана"} - '
                f'{self.salary["to"] if self.salary["to"] == 0 else "ЗП до не указана"} '
                f'{self.currency}\n')


    # def to_dict(self) -> dict:
    #     """ Метод возвращает вакансию в виде словаря """
    #
    #     return {
    #         "name": self.name,
    #         "alternate_url": self.alternate_url,
    #         "salary_from": self.salary_from,
    #         "salary_to": self.salary_to,
    #         "area_name": self.area_name,
    #         "requirement": self.requirement,
    #         "responsibility": self.responsibility,
    #     }


# vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
# vacancies = sorted(vacancies, reverse=True)

# print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
# for i in vacancies:
#     print(i)

# vacancies = [vacancy.to_dict() for vacancy in vacancies]

# a = Vacancy()
#
# print(json.dumps(a.to_dict(), ensure_ascii=False, indent=4))
