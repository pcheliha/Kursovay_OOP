from data.working_with_files import Working_with_files
from data.abs_class import Api
import requests


class HH_api(Api, Working_with_files):
    """
    Класс для работы с HH.ru. принимает желаемую профессию.
    """

    def __init__(self, keyword, page=0):
        self.par = {
            'text': keyword,
            'page': page}

    def get_api(self):
        """
        метод для получения списка вакансий.
        """

        data = requests.get('https://api.hh.ru/vacancies', self.par).json()
        all_vac = []
        for i in data['items']:
            if i['salary'] != None:
                if i['salary']['currency'] == 'RUR':
                    all_vac.append(i)
        for i in all_vac:
            if i['salary']['from'] is None:
                i['salary']['form'] = 0


