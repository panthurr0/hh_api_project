from abc import ABC, abstractmethod


class WorkWithApi(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class SaveFile(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
