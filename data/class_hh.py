import json


from data.abs_class import Api
import requests


class HH_api(Api):
    def __init__(self, keyword, page=0):
        self.par= {
            'text': keyword,
            'page': page}


    def get_api(self):
        data = requests.get("https://api.hh.ru/vacancies", self.par).json()
        all_vac = []
        for i in data['items']:
            if i['salary'] != None:
                if i['salary']['currency'] == 'RUR':
                    all_vac.append(i)

        for i in all_vac:  # Замена значения зп None на 0 для фильтрации.
            if i['salary']['from'] is None:
                i['salary']['from'] = 0

        all_vac.sort(key=lambda x: x['salary']['from'], reverse=True)
        return all_vac


    def hh_save_