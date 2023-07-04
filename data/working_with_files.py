import json


class Working_with_files:
    '''
    работа с файлами.json
    '''


    @staticmethod
    def open_file(file_name):
        '''
        метод для открытия файла. принимает путь и имя для файла

        '''
        with open (file_name, 'r', encoding='utf-8') as file:
            return json.load(file)


