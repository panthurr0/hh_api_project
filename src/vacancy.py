class Vacancy:
    list_vacancies = []

    def __init__(self, name, salary_from, salary_to, url, city, requirement):
        """
        :param name: название вакансии
        :param salary_from: минимальная З/П
        :param salary_to: максимальная З/П
        :param url: ссылка на вакансию
        :param city: город вакансии
        :param requirement: требование от сотрудника
        """
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.city = city
        self.requirement = requirement
        self.list_vacancies.append(self)

    def __lt__(self, other):
        if other.salary_to < self.salary_to:
            return True

    @classmethod
    def cast_to_object_list(cls, hh_vacancies, user_salary):
        """
        Создает CLS из vacancies.json
        :param hh_vacancies: json-файл
        :param user_salary: минимальная З/П, указанная пользователем
        """
        for vacancy in hh_vacancies:
            name = vacancy['name']
            url = vacancy['alternate_url']
            city = vacancy['area']['name']
            requirement = vacancy['snippet']['requirement']

            if vacancy['salary'] is None:
                continue
            elif vacancy['salary']['to'] is not None and vacancy['salary']['from']:
                if vacancy['salary']['from'] >= user_salary:
                    salary_from = vacancy['salary']['from']
                    salary_to = vacancy['salary']['to']
                    cls(name, salary_from, salary_to, url, city, requirement)
                else:
                    continue
            else:
                continue
        return cls.list_vacancies

    @staticmethod
    def print_vacancies(vacancies, count):
        """
        Выводит итоговую информацию по вакансиям
        :param vacancies: отсортированные вакансии
        :param count: сколько пользователь хочет их видеть
        """
        for vacancy in vacancies[:int(count)]:
            print(f"\nВакансия: {vacancy.name}")
            print(f"Заработанная плата:  {vacancy.salary_from} - {vacancy.salary_to}")
            print(f"Город: {vacancy.city}")
            print(f"Требования: {vacancy.requirement}")
            print(f"URL: {vacancy.url}\n")
