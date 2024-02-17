from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy
from src.vacanciesnotfounderror import VacanciesNotFoundError


def user_interaction():
    platforms = ["HeadHunter"]
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос: ").upper()
    vacancies_getter = hh_api.get_vacancies(search_query)

    while True:
        user_salary = input("Введите минимальную заработанную плату: ")
        if user_salary.isdigit():
            break
        print("Вводите только цифры")

    json_saver = JSONSaver()
    json_saver.delete_vacancies()
    json_saver.save_vacancies(vacancies_getter)
    file_vacancies = json_saver.read_file()

    vacancies = Vacancy.cast_to_object_list(file_vacancies, int(user_salary))
    if len(vacancies) == 0:
        raise VacanciesNotFoundError()
    sorted_vacancies = sorted(vacancies)  # сортируем по З/П от большей к меньшей

    while True:
        count = input("Введите количество вакансий для вывода в топ: ")
        if count.isdigit():
            break
        print("Вводите только цифры")

    Vacancy.print_vacancies(sorted_vacancies, count)


if __name__ == "__main__":
    user_interaction()
