from abc import ABC, abstractmethod
import json
from typing import List
from config import OPERATION_PATH


class Saver(ABC):
    """ Абстрактный класс для записи в файл """

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONSaver(Saver):
    """ Класс для записи в json-файл """

    def __init__(self, filepath: str = OPERATION_PATH):
        self.__filepath = filepath

    def add_data(self, vacancies):
        """Сохранить все вакансии в файл"""
        print(f'\nСохранение {len(vacancies)} вакансий в файл')
        self._save_vacancies(vacancies)

    def get_data(self):
        """ Получение данных json """

        try:
            return json.load(open(self.filename))
        except FileNotFoundError:
            return []

    def del_data(self):
        """ Удаление данных из файла """

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)



