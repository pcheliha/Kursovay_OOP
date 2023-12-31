from data.working_with_files import Working_with_files
from data.abs_class import Api
import requests


class Super_job(Api, Working_with_files):
    """
    Класс для работы с Api SuperJob.ru. принимает желаемую професию.
    """
    def __init__(self, keyword, page=1):
        self.par = {
            'keywords': keyword,
            'page': page}
        self.headers = {
            'X-Api-App-Id': 'v3.r.117372392.b2b198f3e65ea1395d521e165431f35de5b98035'
                            '.fee01ee4ea3b163caf63d8a8f6ca0d648e790ea9'}

    def get_api(self):
        """
        метод для получения данных
        :return: отсортированный по ЗП список.
        """
        data = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=self.headers, params=self.par).json()
        all_vac = []
        for i in data['objects']:
            all_vac.append(i)
        all_vac.sort(key=lambda x: x['payment_from'], reverse=True)
        return all_vac




