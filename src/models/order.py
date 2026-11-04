#Файл src/models/order.py
from SFMShop.src.models.product import Product
from SFMShop.src.models.exceptions import InvalidOrderError
class Order:

    def __init__(self, user, products):
        self.user = user
        if products == []:
            raise InvalidOrderError('Заказ невалиден: пустой список товаров')
        self.products = products

    def add_product(self,product):
        if isinstance(product,Product):
            self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total = total + product.price * product.quantity
        return total

