# Файл src/models/product.py
from SFMShop.src.models.exceptions import ValidationError
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "Товар: " + self.name + ", Цена: " + str(self.price) + " руб., Количество: " + str(self.quantity)

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{str(self.price)}', '{str(self.quantity)}')"

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def set_price(self,price):
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self.price = price

    def get_total_price(self):
        return self.price * self.quantity * 0.9

    def check_stock(self):
        return f'В данный момент у нас есть такое количество товара {self.quantity}'

    def update_stock(self,stock):
        if self.quantity > stock:
            self.quantity -=stock

    def get_category(self,product):
        if isinstance(product,Product):
            return True
        return False
product = Product('Ноутбук',20000,10)
print(product.check_stock())
product.update_stock(3)
print(product.check_stock())



