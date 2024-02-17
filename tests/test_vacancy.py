import pytest
import json
from src.vacancy import Vacancy
from config import DATA_TEST


@pytest.fixture
def fixture_class_vacancy_1():
    return Vacancy('Python developer', 60000, 120000, 'blabla.com', 'Moscow', 'Писать на питоне')


@pytest.fixture
def fixture_class_vacancy_2():
    return Vacancy('Сварщик', 20000, 50000, 'zavod.com', 'Nizhny Novgorod', 'Быть трезвым на работе')


@pytest.fixture
def new_file():
    with open(DATA_TEST, encoding='utf-8') as file:
        return json.load(file)


def test_initialization(fixture_class_vacancy_1):
    assert fixture_class_vacancy_1.name == 'Python developer'
    assert fixture_class_vacancy_1.salary_from == 60000
    assert fixture_class_vacancy_1.salary_to == 120000
    assert fixture_class_vacancy_1.url == 'blabla.com'
    assert fixture_class_vacancy_1.city == 'Moscow'
    assert fixture_class_vacancy_1.requirement == 'Писать на питоне'


def test_get_vacancy_list(new_file):
    vacancy = Vacancy.cast_to_object_list(new_file, 50000)
    vacancy2 = Vacancy.cast_to_object_list(new_file, 0)
    false_expected = vacancy < vacancy2
    assert false_expected == False