#Практика Сравнение товаров и заказов
from SFMShop.src.models.order import Order
from SFMShop.src.models.product import Product

products = [
    Product("Ноутбук", 50000, 10),
    Product("Мышь", 1500, 20),
    Product("Клавиатура", 3000, 15)
]

products.sort()

for product in products:
    print(product)

order = Order(1, "Иван", 50000)
print(order)