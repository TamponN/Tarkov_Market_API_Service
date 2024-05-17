from Services.itemService import ItemService
from Services.apiService import Api_service
from application import app
from flask import jsonify, request
from flask_restful import Resource

_itemService = ItemService()
_apiService = Api_service()

class ItemController(Resource):
    """
    
    Класс-контроллер, описывающий методы работы с объектами items
    """
    @staticmethod
    @app.route('/ts/v1/items', methods=['GET'])
    def get_items():
        """
        Получаем все предметы в виде джейсонины
        :return: сериализованный объект items в json
        """
        return jsonify({"items": _itemService.get_all_items()})

    @staticmethod
    @app.route('/ts/v1/items/<string:name>', methods=['GET'])
    def get_item_by_name(name):
        """
        Поиск предмета по имени
        :param name: имя предмета
        :return: сериализованный объект items в json
        """
        return jsonify({"items": _apiService.get_item_by_name(name)})

    @staticmethod
    @app.route('/ts/v1/items/<string:uid>', methods=['GET'])
    def get_item_by_uid(uid):
        """
        Поиск предмета по уникальному идентификатору
        :param uid: уникальный идентификатор предмета
        :return: сериализованный объект items в json
        """
        return jsonify({"items": _apiService.get_item_by_uid(uid)})

    @staticmethod
    @app.route('/ts/v1/items/all/<string:tags>', methods=['GET'])
    def get_all_items_by_tag(tags):
        """
        Поиск предмета по тэгу (патроны, оружия и т.д.)
        :param tags: название категории предметов
        :return: сериализованный объект items в json
        """
        return jsonify({"items": _apiService.get_all_items_by_tag(tags)})
