from src.API_HH import HeadHunterRuAPI
from src.vacancy import Vacancy
from src.vacancy_json import JSONSaver
from typing import List


def top_sort_vac(all_vac: List[Vacancy], top_n: int) -> List[Vacancy]:
    return all_vac[:top_n]


a = HeadHunterRuAPI()
vacancies = a.getting_vacancies("курьер")
vaca = a.validate_data(vacancies)

vacanc = JSONSaver()
vacanc.add_data(vaca)


my_vac = JSONSaver()
vac_data = Vacancy.cast_to_object_list(my_vac.get_data())
vac_data = sorted(vac_data, reverse=True)
top_n_vac = top_sort_vac(vac_data, 5)

for w in top_n_vac:
    print(w)
