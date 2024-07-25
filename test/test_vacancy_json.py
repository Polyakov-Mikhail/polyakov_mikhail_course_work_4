import pytest
from src.vacancy import Vacancy
from src.vacancy_json import JSONSaver
import json
import os


@pytest.fixture
def vacancies():
    return [
        Vacancy(name="Python Developer", url="http://example.com/1", currency="RUR",
                responsibility="Python Test description", salary_from=100000, salary_to=150000),
        Vacancy(name="Java Developer", url="http://example.com/2", currency="RUR",
                responsibility="Java Test description", salary_from=120000, salary_to=170000),
    ]

data_json = "test_vacacies.json"
path_operations = os.path.abspath(data_json)

@pytest.fixture
def json_storage():
    return JSONSaver()


def test_add_vacancies(json_storage, vacancies):
    json_storage.add_data(vacancies)

    saved_vacancies = json_storage.get_data()
    assert len(saved_vacancies) == 2
    assert saved_vacancies[0].id == "1"
    assert saved_vacancies[1].id == "2"

