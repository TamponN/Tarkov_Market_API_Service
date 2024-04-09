from dataclasses import dataclass

@dataclass
class Item:
    """
    Класс для DTO для предметов
    """
    uid: str
    name: str
    price: float
    avg24hPrice: float
    avg7daysPrice: float
    trader: str
    buy_back_price: float
    currency: str
