from abc import ABC, abstractmethod
from config import path_operations
import os
import json


class Saver(ABC):
    """ Абстрактный класс для записи в файл """

    @abstractmethod
    def add_data(self, vacancy):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONSaver(Saver):
    """ Класс для записи в json-файл по пути data/vacancies.json (файл config)"""

    def __init__(self, filepath: str = path_operations):
        self.__filepath = filepath

    def add_data(self, vacancy):
        """Сохранить все вакансии в файл"""
        print(f'\nЯ нашел {len(vacancy)} подходящих вакансий и сохранил в файл {self.__filepath}\n\n')
        with open(self.__filepath, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """ Получение данных json из файла"""
        with open(self.__filepath, encoding='utf-8') as file:
            return json.loads(file.read())

    def del_data(self):
        """ Удаление данных из файла """
        pass
