from Models.itemModel import Item
from Config.sheetConfig import SPREADSHEET_ID
from Services.googleSheetsService import get_service

_sevice = get_service()

class ItemService:
    """
    Класс-сервис для описания методов работы с google sheets
    """
    def get_all_items(self):
        """
        Получение всех предметов из таблицы Google Sheets.
        """
        range_name = 'items_data!A3:H'
        result = _sevice.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=range_name
        ).execute()

        rows = result.get('values', [])

        items = []
        for row in rows:
            if len(row) == 8:
                item = Item(*row)
                items.append(item)

        return items

    # def search_in_sheet(self, search_keyword, service):
    #     """
    #     Поиск предметов в таблице Google Sheets.
    #
    #     :param search_keyword: ключевое слово
    #     :return: список найденных предметов класса Item
    #     """
    #     query = f"select * where B contains '{search_keyword}'"
    #     formula = f'=QUERY(A:D, "{query}", 1)'
    #
    #     # Выполнение запроса
    #     result = service.spreadsheets().values().get(
    #         spreadsheetId=SPREADSHEET_ID,
    #         body={"values": [[formula]]}
    #     ).execute()
    #
    #     return result
