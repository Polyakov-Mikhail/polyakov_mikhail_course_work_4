from src.API_HH import HeadHunterRuAPI
from src.vacancy import Vacancy
from src.vacancy_json import JSONSaver
from typing import List


def top_sort_vac(all_vac: List[Vacancy], top_n: int) -> List[Vacancy]:
    all_vac = sorted(all_vac, reverse=True)
    return all_vac[:top_n]
