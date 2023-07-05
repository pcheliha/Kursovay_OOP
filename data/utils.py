import csv
import json
from data.all_vac import Vacancy
from data.working_with_files import Working_with_files


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def all_vacancy() -> list:
    """
    Функция для единого списка всех вакансий.
    :return: список вакансий с обоих сайтов
    """
    all_vac = []
    data_hh = Working_with_files.open_file('save_file/hh.ru.json')
    for vacancy in data_hh:
        vac = Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary']['from'])
        all_vac.append(vac)

    return all_vac


def create_file_csv():
    """
    Функция для создания файла .csv
    """
    for vacancy in sorted(all_vacancy(), reverse=True):
        with open('save_file/all_vacancy.csv', 'a', encoding='utf=8') as file:
            data = csv.writer(file)
            data.writerow((vacancy.name, vacancy.url, vacancy.zp))


def clear_file_csv():
    """
    Функция для очистки файла .csv
    """
    with open('save_file/all_vacancy.csv', 'w', encoding='utf-8') as file:
        data = csv.writer(file)
        data.writerow(
            ['Вакансия',
             'Ссылка на вакансию',
             'Указаная зарплата'
             ]
        )


def print_top_vac(n=None) -> list:
    """
    Функция для вывода в терминал определённого количества вакансий.
    Возвращает список
    """
    sort_vac = sorted(all_vacancy(), reverse=True)
    return [print(i) for i in sort_vac[:n]]


