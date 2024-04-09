from flask_restful import Resource
from application import app, Api
from flask import render_template
from Services.itemService import ItemService

_itemService = ItemService()

class PageConroller(Resource):
    """
    Заглушка класса-контроллера для будущей работы с web-view
    """
    @staticmethod
    @app.route('/', methods=['GET'])
    def get_items_on_html():
        """
        Выводит все предметы а html шаблон
        """
        items = _itemService.get_all_items()

        return render_template('index.html', items=items)
