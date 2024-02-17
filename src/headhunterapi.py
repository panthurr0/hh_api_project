from src.abstractclasses import WorkWithApi
import requests
import json


class HeadHunterAPI(WorkWithApi):

    def __init__(self):
        self.all_vacancies = []
        self.url = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, keyword):
        params = {
            'text': f'NAME:{keyword}',
            'area': 113,
            'per_page': 100
        }
        response = requests.get(self.url, params=params)
        self.all_vacancies = json.loads(response.text)['items']
        return self.all_vacancies
