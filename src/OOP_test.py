#Файл main.py
from SFMShop.src.models.payment import CardPayment, PayPalPayment
from SFMShop.src.models.product import Product
from SFMShop.src.models.user import User
from SFMShop.src.models.order import Order
from SFMShop.src.models.exceptions import ValidationError
def process_order_system():
    user = User("Иван", "ivan@test.com")
    product1 = Product("Ноутбук", 50000, 2)
    product2 = Product("Мышь", 1500, 3)
    order = Order(user, [product1, product2])
    total = order.calculate_total()
    print("Общая стоимость заказа:", total)

    payments = [
        CardPayment(1000, "1234 5678 9012 3456"),
        PayPalPayment(2000, "test@paypal.com")
    ]

    for payment in payments:
        print(payment.process_payment())

    sorted_products = sorted([product1, product2])
    for product in sorted_products:
        print(product)

    try:
        product.set_price(-1000)
    except ValidationError as e:
        print("Ошибка валидации:", e)

process_order_system()