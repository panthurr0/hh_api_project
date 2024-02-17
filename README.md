# Парсер вакансий HeadHunter'а
Выводит информацию о вакансиях HH по запросу пользователя

## **Структура проекта:**

### **data:**
* [vacancy.json](data/vacancy.json) - файл, в который отправляются вакансии

### **src:** 

* [abstractclasses.py](src/abstractclasses.py) - файл с абстрактными классами
* [heahunterapi.py](src/headhunterapi.py) - класс для работы с API HH'а
* [jsonsaver.py](src/jsonsaver.py) - класс для обработки JSON-файлов
* [vacanciesnotfounderror.py](src/vacanciesnotfounderror.py) - ошибка поиска вакансий
* [vacancy.py](src/vacancy.py) - класс вакансии

### **tests:** 
* [test_vacancy](tests/test_vacancy.py) 



### root:
* [config](config.py)
* [main](main.py) - взаимодействие с пользователем
* [poetry.lock](poetry.lock)
* [pyproject.toml](pyproject.toml)

