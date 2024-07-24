from abc import ABC, abstractmethod
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
    """ Класс для записи в json-файл по пути data/vacancies.json"""

    data_json = "data/vacancies.json"
    path_operations = os.path.abspath(data_json)

    def add_data(self, vacancy):
        """Сохранить все вакансии в файл"""
        print(f'\nЯ нашел {len(vacancy)} подходящих вакансий и сохранил в файл {self.path_operations}\n\n')
        with open(self.path_operations, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """ Получение данных json из файла"""
        with open(self.path_operations, encoding='utf-8') as file:
            return json.loads(file.read())

    def del_data(self):
        """ Удаление данных из файла """
        pass
