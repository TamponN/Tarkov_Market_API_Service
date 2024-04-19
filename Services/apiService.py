from Config.apiConfig import target_url, secret_key
import requests

class Api_service:
    """
    Класс для работы с API. Он описывает методы работы с запросами
    """
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': secret_key
        }
        self.base_url = target_url

    def get_all_items(self):
        finally_url = self.base_url + "items/all"
        response = requests.get(finally_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_item_by_name(self, name):
        """
        Получение предмета по его названию

        :param name: имя предмета
        :return: возвращает джейсонину
        """
        finally_url = self.base_url + "item?q=" + name
        response = requests.get(finally_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_item_by_uid(self, uid):
        """
        Получение предмета по его uid

        :param uid: уникальный идентификатор предмета
        :return: возвращает джейсонину с инфой по предмету
        """
        finally_url = self.base_url + "item?uid=" + uid
        response = requests.get(finally_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_all_items_by_tag(self, tag):
        """
        Получение всех предметов по тегу

        :param tag: категория предметов, которую мы хотим получить
        :return: джейсонина всех предметов, которые совпали
        """
        finally_url = self.base_url + "/items/all?tags=" + tag
        response = requests.get(finally_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
