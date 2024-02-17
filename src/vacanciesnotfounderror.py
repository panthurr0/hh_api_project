class VacanciesNotFoundError(Exception):
    def __init__(self):
        self.message = 'По заданным критериям вакансии не найдены'

    def __str__(self):
        return self.message
