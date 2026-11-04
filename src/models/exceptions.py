# Файл SFMShop.src.models.exceptions.py
class SFMShopException(Exception):
    """Базовое исключение для проекта SFMShop"""
    pass

class ValidationError(SFMShopException):
    """Ошибка валидации данных"""
    pass

class BusinessLogicError(SFMShopException):
    """Ошибка бизнес-логики"""
    pass

class DatabaseError(SFMShopException):
    pass

class InsufficientStockError(BusinessLogicError):
    """Товара недостаточно на складе"""
    pass

class InvalidOrderError(BusinessLogicError):
    """Заказ невалиден"""
    pass

class NegativePriceError(ValidationError):
    """Отрицательная цена"""
    pass

