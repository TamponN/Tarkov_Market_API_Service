from Services.googleSheetsService import get_service
from Models.itemModel import Item
from Services.itemService import ItemService

_itemService = ItemService()

if __name__ == "__main__":
    search_keyword = "Sec"
    service = get_service()
    result = _itemService.get_all_items(service)

    print(result)
