from Services.questService import QuestService
from flask import jsonify, request
from application import app
from flask_restful import Resource

quest_service = QuestService()

class QuestController(Resource):

    @app.route('/ts/v1/quests/<string:trader_name>', methods=['GET'])
    def get_quests_for_trader(trader_name):
        print(f"Request for quests of trader: {trader_name}")  # Diagnostic message
        quests = quest_service.get_quests_for_trader(trader_name)
        if not quests:
            return jsonify({"error": "Квесты для данного торговца не найдены"}), 404
        return jsonify({"quests": quests})

    @app.route('/ts/v1/quest/<string:trader_name>/<string:quest_name>', methods=['GET'])
    def get_quest_details(trader_name, quest_name):
        print(f"Request for quest details: Trader Name: {trader_name}, Quest Name: {quest_name}")  # Diagnostic message
        quest_data = quest_service.get_quest_details(trader_name, quest_name)
        if not quest_data:
            return jsonify({"error": "Подробная информация о квесте не найдена"}), 404
        return jsonify({"quest": quest_data})
