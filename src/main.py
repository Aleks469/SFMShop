# ==================
# УРОК 1: ПЕРЕМЕННЫЕ И СТРОКИ (STR)
# ==================

company_name  = "SFMShop"

welcome_message = "Добро пожаловать в " + company_name + "!"
slogan = company_name + " - лучший выбор для покупок"
email_subject = "Спасибо за покупку в" + company_name

print(welcome_message)
print(slogan)
print(email_subject)

# Практика: Задание 1 - Форматирование имен пользователей

raw_name_1 = "ИВАН"
raw_name_2 = "мария"
raw_name_3 = "пЕТР"
print(raw_name_1.capitalize())
print(raw_name_2.capitalize())
print(raw_name_3.capitalize())

# Практика: Задание 2 - Форматирование цены
price = "1999"
result = "от " + price + " руб."
print(result)

# Практика Задание 3: Нормализация логина и проверка прав

raw_login = "  Логин: IvanPetrov  "
login = raw_login.strip()[7:].lower()
admin = login.startswith('admin')
print('Имя пользователя: ' + login)
print('Это администратор: ' + str(admin))

# Практика: Задание 3 - Расширенная обработка имен.

name_1 = "  ИВАН  "
name_2 = "мария"
name_3 = "  пЕТР  "
name_4 = "АННА"
name_5 = "  олег  "

print(name_1.strip().capitalize())
print(name_2.strip().capitalize())
print(name_3.strip().capitalize())
print(name_4.strip().capitalize())
print(name_5.strip().capitalize())


# ==================
# УРОК 2: ЧИСЛА (INT, FLOAT)
# ==================

# Решение задачи от тимлида - Конвертация валют
exchange_rate = 75.5  # Курс валюты

product_1_price_usd = 29.99
product_2_price_usd = 49.99
product_3_price_usd = 99.99

# Конвертируем в рубли и округляем
product_1_price_rub = round(product_1_price_usd * exchange_rate, 2)
product_2_price_rub = round(product_2_price_usd * exchange_rate, 2)
product_3_price_rub = round(product_3_price_usd * exchange_rate, 2)

print(product_1_price_rub)  # 2264.24
print(product_2_price_rub)  # 3774.25
print(product_3_price_rub)  # 7549.24

# Практика: Задание 1 - Расчет итоговой стоимости заказа
price_per_item = 1500.0
quantity = 3
discount = 0.1 # 10% скидка
final_price = price_per_item * quantity * (1-discount)
final_price_rounded = round(final_price,2)
print(final_price_rounded)

# Практика: Задание 2 - Сдача и купюры
paid = 5000   # сколько дал покупатель
cost = 3750   # стоимость заказа

change = paid - cost
notes = change // 500
rest = change % 500
print(f'Сдача: {change} руб; купор по 500: {notes}, остаток: {rest} руб.')

# Практика: Задание Расширенный расчет стоимости заказов

# Заказ 1: с обычной скидкой
order_1_price = 2000.0
order_1_quantity = 2
order_1_discount = 0.15

print('Заказ 1:')
print(f'Исходная цена: {order_1_price * 2} руб.')
print(f'Размер скидки: {order_1_price * 2 * order_1_discount} руб.')
print(f'Итоговая цена: {round(order_1_price * 2 * (1 - order_1_discount),2)} руб.')
print()

# Заказ 2: без скидки
order_2_price = 3000.0
order_2_quantity = 1
order_2_discount = 0.0
print('Заказ 2 :')
print(f'Исходная цена: {order_2_price} руб.')
print(f'Размер скидки: {order_2_price * order_2_discount} руб.')
print(f'Итоговая цена: {round(order_2_price * (1 - order_2_discount),2)} руб.')
print()

# Заказ 3: с большой суммой
order_3_price = 5000.0
order_3_quantity = 3
order_3_discount = 0.2

print('Заказ 3:')
print(f'Исходная цена: {order_3_price * 3} руб.')
print(f'Размер скидки: {order_3_price * 3 * order_3_discount} руб.')
print(f'Итоговая цена: {round(order_3_price * 3 * (1 - order_3_discount),2)} руб.')

# ==================
# УРОК 3: УСЛОВНЫЕ ОПЕРАТОРЫ
# ==================

# Решение задачи от тимлида - Проверка условий заказа
user_age = 20
product_quantity = 5

# Проверяем оба условия через and
if user_age >= 18 and product_quantity > 0:
    print("Заказ можно оформить")
else:
    # Определяем причину отказа
    if user_age < 18:
        print("Заказ нельзя оформить: пользователь несовершеннолетний")
    if product_quantity <= 0:
        print("Заказ нельзя оформить: товара нет на складе")

print()
# Практика: Задание 1 - Определение размера скидки
order_total = 6000

if order_total >= 10000:
    print('Размер скидки: 15.0%')
elif order_total >= 5000:
    print('Размер скидки: 10.0%')
else:
    print('размер скидки: 5.0%')

#Практика: Задание Валидация и расчет стоимости заказа
order_total = 6000
if order_total < 0:
    print('Ошибка: сумма заказа не может быть отрицательной')
else:
    if order_total > 10000:
        discount_rate = 0.15
    elif order_total > 5000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05


print(f'Исходная сумма {order_total} руб.')
print(f'Размер скидки: {discount_rate * 100}%')
print(f'Размер скидки: {discount_rate * order_total} руб.')
print(f'Итоговая стоимость: {round(order_total - (discount_rate * order_total),2)} руб.')

# Практика: Задание 2 - Доступ пользователя
user_age = 17
user_balance = 500
order_total = 1000
requested_qty = 3
in_stock = 5
if user_age >= 18 and user_balance >= order_total and in_stock >=requested_qty:
    print("Заказ можно оформить")
else:
    if user_age < 18:
        print('Отказ: пользователь несовершеннолетний')
    if user_balance < order_total:
        print('Отказ: недостаточно средств')
    if in_stock < requested_qty:
        print('Отказ: нет нужного количества на складе')

print()
# Практика: Задание 3 - Расчёт стоимости доставки
order_total = 3500
city = "Казань"
if order_total > 5000:
    delivery_cost = 0
elif city =='Москва' or city == 'Санкт-Петербург':
    delivery_cost = 300
else:
    delivery_cost = 500
print(f'Стоимость доставки {delivery_cost} руб.')


prices = [1500, 2300, 890, 4500, 1200]
a = prices.sort()
print(a) # [890, 1200, 1500, 2300, 4500]


# ==================
# УРОК 4: СПИСКИ (LIST)
# ==================

# Решение задачи от тимлида - Подсчет общей суммы заказов
orders = [1500, 2300, 890, 4500, 1200]

# Используем встроенные функции
total = sum(orders)
count = len(orders)
average = total / count

print("Общая сумма:", total)
print("Средний чек:", average)

print()


# Практика: Задание 1 - Сортировка и поиск цен товаров
prices = [1500, 2300, 890, 4500, 1200]
lst = prices.copy()
lst.sort(reverse=True)
print(f'Отсортированные цены: {lst}')
print(f'Максимальная цена: {max(lst)}')
print(f'Минимальная цена: {min(lst)}')

# Практика: Задание 2 - Копирование списка заказов
orders = [1500, 2300, 890]
archive = orders[:]
archive.append(1300)
print(f'Текущие заказы: {orders}')
print(f'Архив заказов: {archive}')


# ==================
# УРОК 5: ЦИКЛЫ (FOR, WHILE)
# ==================

# Решение задачи от тимлида - Поиск заказов с суммой больше 5000
orders = [3000, 6000, 4500, 8000, 2000]

for order in orders:
    if order > 5000:
        print("Большой заказ:", order)
print()

# Практика: Задание 1 - Поиск товаров с ценой больше 1000
prices = [500, 1500, 800, 2000, 1200]
for el, price in enumerate(prices):
    if price > 1000:
        print(f'Товар {el+1}: {price} руб.')

# Практика: Задание 2 - Сумма корзины со скидкой
prices = [500, 1500, 800, 2000, 1200]
prices_sum = sum(prices)
if prices_sum > 5000:
    print(f'Итоговая сумма: {prices_sum * 0.9} руб.')
else:
    print(f'Итоговая сумма : {prices_sum} руб.')

print()
# Практика: Расширенная обработка товаров
price_1 = 500
price_2 = 1500
price_3 = 800
price_4 = 2000
price_5 = 1200
lst = [price_1, price_2, price_3, price_4, price_5]
count = 0
for i, price in enumerate(lst):
    if price > 1000:
        count +=1
        print(f'Товар {i+1}: {price} руб.')
if count == 0:
    print('Товаров с ценой больше 1000 не найдено.')
else:
    print()
    print(f'Количество товаров с ценой больше 1000: {count}')
    print()
    max_el = max(lst)
    ind = lst.index(max_el) + 1
    print(f'Товар с максимальной ценой: Товар {ind}, цена {max_el} руб.')

# Практика Управление корзиной покупок
cart = []
names = ["Ноутбук", "Мышь", "Клавиатура"]
prices = [50000, 1500, 3000]
for name, price in zip(names,prices):
    cart.append([name,price])
print(f'Корзина после добавления товаров: {cart}')
cart.remove(['Мышь', 1500])
print(f'Корзина после удаления: {cart}')
cart.sort()
print(f'Корзина после сортировки: {cart}')
if len(cart) > 0:
    print(f'Самый дорогой товар: {max(cart,key = lambda x: x[1])}')

print()
#dict comprehensions
# Список названий товаров SFMShop
product_names = ["Ноутбук", "Мышь", "Клавиатура"]
product_prices = [50000, 1500, 3000]

prod_dict = {product_names[i] : product_prices[i] for i in range(len(product_names))}

print(prod_dict)

# ==================
# УРОК 6: СЛОВАРИ (DICT) И МНОЖЕСТВА (SET)
# ==================

# Решение задачи от тимлида - Данные пользователя в словаре и уникальные посетители
# Хранение данных пользователя в словаре
user = {
    "name": "Иван Иванов",
    "email": "ivan@example.ru",
    "phone": "+7 999 123-45-67"
    }

# Получение данных по ключу
print("Имя:", user["name"])
print("Email:", user["email"])

# Подсчет уникальных посетителей через множество
visitors = {"user_123", "user_456", "user_123", "user_789"}
unique_count = len(visitors)

print("Уникальных посетителей:", unique_count)

# Практика: Задание 1 - Работа со словарем товара
product = {
    "name": "Ноутбук",
    "price": 50000,
    "quantity": 5
    }
product.update({'quantity': 10})
print(f'Ключи словаря {product.keys()}')
print(f'Значения словаря {product.values()}')

# Практика: Задание 2 - Словарное включение из списка товаров
catalog = [["Ноутбук", 50000], ["Мышь", 1500], ["Клавиатура", 3000]]
catalog_price = {item[0]: item[1] for item in catalog}
print(catalog_price)
print(f'Цена мыши: {catalog_price['Мышь']}')

# Практика Система хранения данных о пользователях и товарах
users = {}

products = {
    "Ноутбук": {
        "price": 50000,
        "category": "Электроника"
    },
    "Мышь": {
        "price": 1500,
        "category": "Аксессуары"
    }
}

visitors = set()

users[1] = {'name' : 'Иван', 'email' : 'ivan@test.ru'}
print(f'Пользователь добавлен: {users[1]}')
print(f"Цена товара '{list(products.keys())[0]}': {products['Ноутбук']['price']} руб.")
visitors.add('user_123')
print(f"Посетитель 'user_123' был на сайте: {bool('user_123' in visitors)}")


# ==================
# УРОК 7: КОРТЕЖИ (TUPLE)
# ==================

# Решение задачи от тимлида - Хранение размеров товара в кортеже
# Хранение размеров в кортеже
dimensions = (30, 20, 15)

# Распаковка для расчета объема
length, width, height = dimensions
volume = length * width * height

print("Размеры товара:", dimensions)
print("Объем упаковки:", volume)

print()
# Практика: Задание 1 - Работа с кортежами
coordinate = (10,20)
x, y = coordinate
loc = {coordinate : 'Офис'}
print(f'Координата x: {x}')
print(f'Координата y: {y}')
print(f'Название места: {loc[coordinate]}')

# Практика: Задание 2 - Распаковка координат склада
warehouse = (55, 37, "Москва")
wide, longitude, city = warehouse
print(f'Склад в городе {city}: широта {wide}, долгота {longitude}')

#Практика Система хранения координат доставки
# Координаты доставки по ID заказа: ключ - ID, значение - кортеж (широта, долгота)
delivery_coordinates = {
    1: (55.7558, 37.6173),
    2: (59.9343, 30.3351),
}
order1 = 1
order2 = 2
if order1 in delivery_coordinates:
    print(f'Координаты заказа 1: {delivery_coordinates[1]}')
    wide1, longitude1 = delivery_coordinates[1]
    print(f'Широта: {wide1}')
    print(f'Долгота: {longitude1}')
if order2 in delivery_coordinates:
    print(f'Координаты заказа 2: {delivery_coordinates[2]}')
    wide2, longitude2 = delivery_coordinates[2]
    print(f'Широта: {wide2}')
    print(f'Долгота: {longitude2}')
print(f'Координаты заказа 3: {delivery_coordinates.get(3,'Заказ не найден')}')

print()


# ==================
# УРОК 8: ФУНКЦИИ
# ==================

# Решение задачи от тимлида - Валидация email и гибкое логирование
def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False

# Проверка всех email через функцию
email_1 = "ivan@example.ru"
email_2 = "petr@test"
email_3 = "invalid-email"

result_1 = validate_email(email_1)
result_2 = validate_email(email_2)
result_3 = validate_email(email_3)

print("Email 1 валиден:", result_1)
print("Email 2 валиден:", result_2)
print("Email 3 валиден:", result_3)

print()

# Практика: Задание 1 - Функция расчета цены со скидкой
def final_price(price, discount):
    return price * (1 - discount)

product1 = final_price(1000,0.1)
product2 = final_price(2000,0.8)

print(f'Цена товара 1 со скидкой: {round(product1,2)}')
print(f'Цена товара 2 со скидкой: {round(product2,2)}')

# Практика: Задание 2 - Функция суммирования с *args
def sum_all(*args):
    total = 0
    for el in args:
        total += el
    return total

two_number = sum_all(3,4)
four_number = sum_all(5,6,1,2)
without_arg = sum_all()
print(f'Сумма двух чисел: {two_number}')
print(f'Сумма четырех чисел: {four_number}')
print(f'Сумма без аругментов: {without_arg}')

# Практика: Задание 3 - Функция создания описания товара с **kwargs
def describe_product(product_name,**kwargs):
    lst = []
    for el in kwargs:
        lst.append(f'{el}: {str(kwargs[el])}')
    res = f'{product_name} ({", ".join(lst)})'
    return res
info_1 = describe_product("Ноутбук", цена=50000, бренд="Lenovo", вес=2.1)
info_2 = describe_product("Мышь", цвет="черный")
info_3 = describe_product("Клавиатура")

print(info_1)
print(info_2)
print(info_3)

# Практика Набор функций для работы с заказами
def calculate_order_total(price, quantity, discount):
    return round((price * quantity) * (1 - discount),2)

def check_stock_availability(stock_quantity, required_quantity):
    if stock_quantity >= required_quantity:
        return True
    return False

def format_order_info(order_id, total):
    return f'Заказ #<{order_id}, Сумма: <{total}> руб.'

check = check_stock_availability(10,3)
if check:
    print(f'Товар доступен: {check}')
    cost = calculate_order_total(1000,3,0.1)
    formatted = format_order_info(1,cost)
    print(formatted)

print()

# Практика: Задание 1 - Безопасный расчет стоимости заказа

def safe_order_total(items):
    # Твой код здесь
    count = 0
    result = 0
    for item in items:
        try:
            item_total = item['price'] * item['quantity']
            print(f"{item['name']}: {item['price'] * item['quantity']} руб.")

        except KeyError:
            print(f'Ошибка в товаре {item["name"]}: отсутствует обязательное поле')
        except TypeError:
            print(f'Ошибка в товаре {item["name"]}  неверный тип данных для расчета')
        else:
            count += 1
            result += item_total
    print(f'Обработано товаров: {count} из {len(items)} ')
    return result
# Тестовые данные
test_items = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 2},
    {"name": "Клавиатура"},
    {"name": "Монитор", "price": None, "quantity": 1},
    {"name": "Наушники", "price": 3000, "quantity": 3}
    ]
result = safe_order_total(test_items)
print("Общая стоимость: " + str(result))

# Практика: Задание 2 - Валидация данных пользователя

print()

def validate_user_data(user_data):
    total = 0
    #проверка для имени
    try:
        if user_data['name'] and isinstance(user_data['name'],str):
            print('Имя: OK')
            total +=1
        else:
            raise KeyError
    except KeyError:
        print('Имя: ошибка - имя не может быть пустым')

    #проверка для возраста
    try:
        if int(user_data['age']) and 18 <= int(user_data['age']) < 121:
            total +=1
            print(f'Возраст: ОК ({int(user_data['age'])})')
        else:
            raise ValueError
    except ValueError:
        print(('Возраст: ошибка - невозможно преобразовать в число'))

    #проверка email
    try:
        if '@' in user_data['email']:
            total +=1
            print('Email: ОК')
        else:
            raise
    except:
        print('Email: ошибка - email должен содержать символ @')

    #проверка номера телефона
    try:
        phone = user_data['phone']
        clean_phone = phone.replace(' ','').replace('-','')
        if clean_phone.isdigit():
            total +=1
            print('Phone: OK')
        else:
            raise
    except:
        print('Телефон: ошибка - телефон должен содержать только цифры')

    if total == len(user_data):
        print('Результат: все поля корректны')
    else:
        print('Результат: найдены ошибки')
# Тестовые данные
user_1 = {"name": "Иван Петров", "age": "25", "email": "ivan@sfmshop.ru", "phone": "89001234567"}
user_2 = {"name": "", "age": "молодой", "email": "неверный_email", "phone": "89oo1234567"}

print("Проверка пользователя 1:")
result_1 = validate_user_data(user_1)
print()
print("Проверка пользователя 2:")
result_2 = validate_user_data(user_2)


# Практика: Задание 3 - Обработка корзины покупок

print()

def add_to_cart(cart, name, price, quantity):
    try:
        if not name:
            raise TypeError
        if price < 0 or quantity < 0:
            raise ValueError
        total = price * quantity
        cart.append({'name': name, 'price': total})
        print(f'Добавлен: {name} ({price} руб. x {quantity})')

    except TypeError:
        print('Ошибка: название товара не может быть пустым')
    except ValueError:
        print('Ошибка: цена и количество должны быть положительными')

def remove_from_cart(cart, index):
    try:
        if len(cart) -1 >= index:
            res = cart.pop(index)
            print(f'Удален: {res['name']}')
        else:
            raise IndexError
    except IndexError:
        print(f'Ошибка: товар с индексом {index} не найден в корзине')


def get_cart_summary(cart):
    print('---Корзина---')
    res_sum = 0

    for i in range(len(cart)):
        print(f'{i+1}. {cart[i]['name']}: {cart[i]['price']} руб.')
        res_sum += cart[i]['price']
    print(f'Итого: {res_sum} руб. (товаров: {len(cart)})')
# Тестирование
cart = []
add_to_cart(cart, "Ноутбук", 50000, 1)
add_to_cart(cart, "Мышь", 1500, 2)
add_to_cart(cart, "", 3000, 1)
add_to_cart(cart, "Наушники", -500, 1)
remove_from_cart(cart, 1)
remove_from_cart(cart, 10)
get_cart_summary(cart)

print()

# ==================
# УРОК 9: РАБОТА С ФАЙЛАМИ
# ==================

# Решение задачи от тимлида - Сохранение лога ошибок
error_message = "Ошибка: товар не найден на складе\n"

# Использование контекстного менеджера и режима 'a'
with open("data/errors.log", "w", encoding="utf-8") as file:
   file.write(error_message)
# Файл автоматически закрывается

# Практика: Задание 1 - Чтение и запись товаров
# Сначала создай файл data/products.txt с содержимым:
# Ноутбук
# Мышь
# Клавиатура
products = ['Ноутбук\n','Мышь\n','Клавиатура\n']
with open('data/products.txt','w',encoding='utf-8') as file:
    file.writelines(products)

with open('data/products.txt','r',encoding='utf-8') as file:
    lines = file.readlines()

with open('data/products_with_prices.txt','w',encoding='utf-8') as file:
    for line in lines:
        file.writelines(f'{line.strip()} - 1000 руб.\n')

# Практика: Задание 2 - Подсчёт заказов в файле
# Сначала создай файл data/orders.txt с содержимым:
ord = ['Ноутбук\n','Мышь\n','Клавиатура\n','Системник\n']
with open('data/orders.txt','w',encoding='utf-8') as file:
    file.writelines(ord)

with open('data/orders.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
orders = [line for line in lines if line.strip()]
print(f'Заказов в файле: {len(orders)}')

#Практика Обработка заказов из файла
# В файле src/main.py
# Сначала создай файл data/orders.txt с содержимым:
# 1:1000:новый
# 2:2000:обработан
# 3:1500:новый
# 4:3000:новый
data = ['1:1000:новый\n','2:2000:обработан\n','3:1500:новый\n','4:3000:новый\n']
with open('data/orders.txt','w',encoding='utf-8') as file:
    file.writelines(data)
try:
    with open('data/orders.txt','r',encoding='utf-8') as file:
        lines = file.readlines()
    lst = [line.split(':') for line in lines if line.strip()]
    total = 0
    count = 0
    for i in range(len(lst)):
        if lst[i][2].strip() =='новый':
            total += int(lst[i][1])
            count += 1
except FileNotFoundError:
    print('Файл не найден')

with open('data/processed_orders.txt','w',encoding='utf-8') as file:
    file.write(f'Обработано заказов: {count}\n')
    file.write(f'Общая сумма: {total} руб.\n')

#  TESTING MODULES JSON
order = {
    "user": "Иван Петров",
    "products": [
        {"name": "Ноутбук", "price": 60000, "quantity": 1},
        {"name": "Мышь", "price": 1500, "quantity": 2},
    ],
    "total": 63000,
}
import json
with open('data/ordes.json','w',encoding='utf-8') as file:
    json.dump(order,file,ensure_ascii=False,indent=2)

with open('data/ordes.json','r',encoding='utf-8') as file:
    loaded_order = json.load(file)




# ==================
# УРОК 10: ИМПОРТИРОВАНИЕ МОДУЛЕЙ, СОЗДАНИЕ СВОИХ МОДУЛЕЙ
# ==================

# Решение задачи от тимлида - Генерация промо-кода через модуль random
import random

promo_number = random.randint(100000, 999999)
promo_code = "PROMO" + str(promo_number)

print("Промо-код:", promo_code)
print()
# Практика: Задание 1 - Создание модуля расчетов
# Импорт своего модуля
from utils.calculations import calculate_discount

# Использование функций
discount1 = calculate_discount(1000, 0.1)
discount2 = calculate_discount(1000, 0.75)

print("Скидка для товара 1:", discount1)
print("Скидка для товара 2:", discount2)
# Практика: Задание 2 - Функция скидки в отдельном модуле
import SFMShop.discounts

price = SFMShop.discounts.apply_discount(1000,0.1)
print(f'Цена со скидкой: {price}')
print()

#Практика Модульная структура проекта
#Файл src/main.py
from utils.calculations import calculate_discount, calculate_delivery, calculate_final_price
from utils.validators import validate_age, validate_email

age_valid = validate_age(20)
email_valid = validate_email('ivan@test.ru')
print(f'Возраст валиден: {age_valid}')
print(f'Email валиден: {email_valid}')
if age_valid and email_valid:
    discount = calculate_discount(1000, 0.1)
    delivery = calculate_delivery(5)
    total = calculate_final_price(1000,discount, delivery)
    if age_valid and email_valid:
        print(f'Итоговая стоимость заказа: {total} руб.')

print()

# ==================
# УРОК 11: ОБЛАСТИ ВИДИМОСТИ ПЕРЕМЕННЫХ
# ==================

# Решение задачи от тимлида - Глобальная константа стоимости доставки
# Глобальная константа определена в начале секции, до использования
BASE_DELIVERY_COST = 100

def calculate_order_total(price, quantity):
    # Используем глобальную константу (читаем, не изменяем)
    total = price * quantity + BASE_DELIVERY_COST
    return total

result = calculate_order_total(1000, 3)
print("Итого:", result)

# Практика: Задание 1 - Работа с глобальными переменными
discount = 0.1
def calculate_discount(price):
    return price * (1-discount)

res1 = calculate_discount(1000)
print(f'Цена со скидкой {discount * 100}%: {res1}')

discount = 0.2
res2 = calculate_discount(1000)
print(f'Цена со скидкой {discount * 100}%: {res2}')

# Практика: Задание 2 - Счётчик обработанных заказов
processed = 0
def handle_order():
    global processed
    processed +=1
    return processed
handle_order()
handle_order()
handle_order()
print(f'Обработано заказов: {processed}')

#Практика Система настроек приложения
BASE_DISCOUNT = 0.1
BASE_DELIVERY_COST = 100
def calculate_order_price(price, quantity):
    subtotal = price * quantity
    return subtotal - subtotal * BASE_DISCOUNT + BASE_DELIVERY_COST
def update_discount(new_discount):
    global BASE_DISCOUNT
    BASE_DISCOUNT = new_discount

cost_1 = calculate_order_price(1000,2)
print(f'Стоимость заказа (скидка {BASE_DISCOUNT * 100}%): {cost_1}')

update_discount(0.15)
cost_2 = calculate_order_price(1000,2)
print(f'Стоимость заказа (скидка {BASE_DISCOUNT * 100}%): {cost_2}')

print()

# ==================
# УРОК 12: F-СТРОКИ, МЕТОДЫ СТРОК, ОТЛАДКА
# ==================

# Решение задачи от тимлида - Форматирование сообщения для лога через f-строку
order_id = 123
order_total = 5000
order_status = "новый"

# Использование f-строки вместо сложной конкатенации
message = f"Заказ #{order_id}, Сумма: {order_total} руб., Статус: {order_status}"
print(message)

# Практика: Задание 1 - Форматирование информации о товаре

def formatted(name, price, quantity):
    info = f'Информация о товаре: Товар: {name}, Цена: {price}, Количество: {quantity}'
    return info
result = formatted('Ноутбук', 50000, 10)
print(result)

products = ['Ноутбук','Мышь','Клавиатура']
result_product = ', '.join(products)
print(f'Товары: {result_product}')

# Практика: Задание 2 - Форматирование цены до копеек
price = 1234.5
print(f'{price:.2f} руб.')

print()

# ==================
# УРОК 13: РАБОТА С ДАТАМИ И ВРЕМЕНЕМ
# ==================

# Решение задачи от тимлида - Расчет даты доставки через datetime и timedelta
from datetime import datetime, timedelta

# Создание объекта datetime
order_date = datetime.strptime("2024-01-15 10:00:00", "%Y-%m-%d %H:%M:%S")

# Расчет даты доставки
delivery_days = 3
delivery_date = order_date + timedelta(days=3)

print("Дата заказа:", order_date)
print("Дата доставки:", delivery_date)

order_date = datetime(2024, 1, 15)
delivery_date = datetime(2024, 1, 18)
days = (delivery_date - order_date).days
print("Дней до доставки:", days)

# Практика: Задание 1 - Работа с датами
today = datetime.now()
did_order = datetime(2026,10,20,16,24,00)
issued_order = datetime(2026,10,24,12,30,00)
print(f'Текущее время {today.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Дата заказа {did_order.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Дата доставки {issued_order.strftime("%Y-%m-%d %H:%M:%S")}')
print(f'Дней до доставки: {(issued_order - did_order).days}')


# Практика: Задание 2 - Сколько дней до дедлайна
from datetime import date

start = date(2026, 12, 1)
deadline = date(2026, 12, 31)
print(f'До дедлайна: {(deadline - start).days}')

# Практика: Система расчета сроков доставки
from datetime import datetime
def calculate_delivery_date(order_date, delivery_days):
    return order_date + timedelta(days=delivery_days)

def log_order_creation(order_id, order_time):
    return f'Заказ #{order_id} создан: {order_time.strftime("%Y-%m-%d %H:%M:%S")}'


order_date = datetime(2024, 1, 15, 10, 0, 0)
deliv_date = calculate_delivery_date(order_date,3)
print(f'Дата доставки: {deliv_date.strftime("%Y-%m-%d %H:%M:%S")}')

order_time = datetime(2024, 1, 15, 14, 30, 0)
create_order = log_order_creation(123,order_time)
print(create_order)

print()

# ==================
# УРОК 14: РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
# ==================

# Решение задачи от тимлида - Надежная валидация email и телефона через regex
import re

def validate_email(email):
    pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    result = re.fullmatch(pattern,email)
    return result is not None

def validate_phone(phone):
    pattern = r"\+7[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}"
    result = re.fullmatch(pattern,phone)
    return result is not None

email = "ivan@example.ru"
phone = "+7 999 123-45-67"

print("Email валиден:", validate_email(email))
print("Телефон валиден:", validate_phone(phone))

# Практика: Задание 1 - Валидация email через регулярное выражение
def validate_email(email):
    pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    result = re.fullmatch(pattern,email)
    return result is not None

email_1 = 'ivan@example.ru'
email_2 = 'invalid'
email_3 = 'test@'
print(f'Email {email_1} валиден: {validate_email(email_1)}')
print(f'Email {email_2} валиден: {validate_email(email_2)}')
print(f'Email {email_3} валиден: {validate_email(email_3)}')

# Практика: Задание 2 - Извлечь все цены из текста
import re
text = "Ноутбук 50000, мышь 800, клавиатура 1500"
pattern = r"\d+"
res = re.findall(pattern,text)
print(f'Найдены цены: {res}')

#Практика Система валидации данных пользователя
import re
def validate_email_regex(email):
    pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    return re.fullmatch(pattern,email) is not None

def validate_phone_regex(phone):
    pattern = r'\+7[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}'
    return re.fullmatch(pattern,phone) is not None

def clean_input(inp):
    cleaned = re.sub(r"[^\w\s]","", inp)
    return cleaned

def extract_email_from_text(text):
    return re.search(r"support@example\.ru",text).group()

phone = '+7 999 123-45-67'
email = 'ivan@test.ru'
text = '"Заказ #123!!! Сумма: 5000 руб."'
text_email = "Свяжитесь с нами: support@example.ru для помощи"
print(f'Email валиден: {validate_email_regex(email)}')
print(f'Телефон валиден: {validate_phone_regex(phone)}')
print(f'Очищенный текст: {clean_input(text)}.')
print(f'Извлеченный текст: {extract_email_from_text(text_email)}')

print()

#if match is not None:    group используется если надо найти само значение!!!! без него чисто будет выдавать re.Match ....
#    print(match.group())

# ==================
# УРОК 15: КЛАССЫ (ООП)
# ==================

# Решение задачи от тимлида - класс Product
# Класс лежит в src/models/product.py, здесь только используем его
from models.product import Product

laptop = Product("Ноутбук", 50000, 10)
total = laptop.get_total_price()
print("Общая стоимость:", total)

# Практика: Задание 1 - Классы User и Order
from models.product import Product
from models.order import Order
from models.user import User
user_1 = User('Alex','prikol@mail.ru')
product_1 = Product('Ноутбук',50000,1)
product_2 = Product('Мышь',1500,2)
product = [product_1,product_2]
ord = Order(user_1,product)
print(f'Общая стоимость заказа: {ord.calculate_total()}')

# Практика: Задание 2 - Валидация цены через @property
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if new_price < 0:
            print('Ошибка: цена не может быть отрицательной')
            return
        self._price = new_price

order_1 = Product('Petya',50000)
print(f'Цена: {order_1.price}' )
order_1.price = -500
print(f'Цена после ошибки: {order_1.price}')

print()

# ==================
# УРОК 16: ПРИНЦИПЫ ООП
# ==================

# Решение задачи от тимлида - иерархия платежей
# (наследование, инкапсуляция, полиморфизм, абстракция)
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        raise NotImplementedError("Метод должен быть переопределен")


class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.__card_number = card_number # Приватный атрибут

    def process_payment(self):
        # Доступ к приватному атрибуту только изнутри класса
        masked_card = "**** " + self.__card_number[-4:]
        return "Оплата картой " + masked_card + ": " + str(self.amount) + " руб."


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self._email = email # Защищенный атрибут

    def process_payment(self):
        return "Оплата PayPal (" + self._email + "): " + str(self.amount) + " руб."

# Использование полиморфизма
payments = [
    CardPayment(1000, "1234 5678 9012 3456"),
    PayPalPayment(2000, "user@paypal.com"),
]

for payment in payments:
    print(payment.process_payment()) # Единый интерфейс

# Практика: Задание 1 - Наследование
class Delivery:

    def get_description(self):
        return 'Способ доставки'


class StandardDelivery(Delivery):

    def get_description(self):
        return 'Стандартная доставка: 3-5 дней'


class ExpressDelivery(Delivery):

    def get_description(self):
        return 'Экспресс-доставка: 1 день'

lst = [StandardDelivery(), ExpressDelivery()]
for ord in lst:
    print(ord.get_description())


# Практика: Задание 2 - Полиморфизм и инкапсуляция
class Product:

    def __init__(self,name,price):
        self.name = name
        self._price = price

    def final_price(self):
        return self._price


class DiscountProduct(Product):
    def __init__(self,name,price,discount):
        super().__init__(name,price)
        self.__discount = discount

    def final_price(self):
        return self._price * (1 - self.__discount)


class GiftProduct(Product):

    def final_price(self):
        return 0

lst = [Product('Кружка',500), DiscountProduct('Футболка',1000,0.2), GiftProduct('Открытка',500)]
for prod in lst:
    print(f'{prod.name}: {prod.final_price()} руб.')


# Файл SFMShop/src/main.py

from SFMShop.src.models.payment import CardPayment, PayPalPayment

payments = [
    CardPayment(1000, "1234 5678 9012 3456"),
    PayPalPayment(2000, "user@paypal.com")
]
for el in payments:
    print(el.process_payment())

print()


# ==================
# УРОК 17: МАГИЧЕСКИЕ МЕТОДЫ
# ==================

# Решение задачи от тимлида - читаемый вывод и сравнение товаров
# В src/models/product.py добавлены __str__, __repr__, __lt__, __eq__

from SFMShop.src.models.product import Product

laptop = Product('Ноутбук',50000,510)
print(laptop)

products = [
    Product("Ноутбук", 50000, 10),
    Product("Мышь", 1500, 20),
    Product("Клавиатура", 13000, 15),
]
products.sort()
for product in products:
    print(product)

print()
# Файл src/main.py
# Практика: Задание 1 - Добавление __str__ и __repr__  в product.py

laptop = Product("Ноутбук", 50000, 10)
print(laptop)
print(repr(laptop))

# Практика: Задание 2 - Корзина с __len__ и __add__
class Cart:
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self,other):
        return Cart(self.owner,self.items + other.items)

    def __str__(self):
        return f'Корзина {self.owner}: {len(self.items)} товаров на сумму {sum(self.items)} руб.'

cart_1 = Cart("Иван", [50000, 1500])
cart_2 = Cart("Иван", [3000, 2500])
print(cart_1 + cart_2)

print()

# #Практика Сравнение товаров и заказов                         Задание ментора закомментил ибо тогда траблы с order и product
from SFMShop.src.models.order import Order
from SFMShop.src.models.product import Product
#
# products = [
#     Product("Ноутбук", 50000, 10),
#     Product("Мышь", 1500, 20),
#     Product("Клавиатура", 3000, 15)
# ]
#
# products.sort()
#
# for product in products:
#     print(product)
#
# order = Order(1, "Иван", 50000)
# print(order)
#
# print()

# ==================
# УРОК 18: ОБРАБОТКА ИСКЛЮЧЕНИЙ (TRY/EXCEPT, RAISE)
# ==================

# Решение задачи от тимлида - валидация через raise и обработка через try/except
# Проверки добавлены в src/models/product.py и src/models/user.py
from SFMShop.src.models.product import Product
from SFMShop.src.models.user import User

try:
    product = Product('Монитор',50000,-10)
except ValueError as e:
    print(f'Ошибка при создании товара: {e}')
    product = Product('Монитор',50000, 10)


try:
    user = User("Иван", "неверный_email")
except ValueError as e:
    print("Ошибка при создании пользователя:", e)
    user = User("Иван", "default@example.ru")

# Практика: Задание 1 - Обработка ошибок деления
def divide(a,b):
    try:
        res = a / b
        return res
    except ZeroDivisionError as e:
        print(f'Ошибка {e}')
        return None
    except TypeError as e:
        print(f'Ошибка {e}')
    else:
        return res

print(f'Результат: {divide(5,1)}')
print(divide(5,0))
print(divide('a',5))

# Практика 2 Резервирование товара на складе
class Warehouse:

    def __init__(self,stock):
        self.stock = stock

    def reserve(self,product, quantity):
        if quantity <= 0:
            raise ValueError('Количество должно быть больше 0')
        if product not in self.stock:
            raise KeyError('Данного товара нет на складе')
        if self.stock[product] < quantity:
            raise ValueError(f'Ошибка: Недостаточно товара: запрошено {quantity}, в наличии {self.stock[product]}')
        self.stock[product] -=quantity
        return self.stock[product]

warehouse = Warehouse({'Ноутбук' : 5})
requests = [("Ноутбук", 3), ("Мышь", 1), ("Ноутбук", 10), ("Ноутбук", 0)]
for k, v in requests:
    try:
        product = warehouse.reserve(k,v)
        print(f'Зарезервировано {v} ({k}), осталось {product}')
    except KeyError:
        print(f'Нет Такого товара: {k}')
    except ValueError as e:
        print(f'Ошибка: {e}')

print()

# Практика Обработка исключений в классах
# from SFMShop.src.models.product import Product
# from SFMShop.src.models.user import User
# from SFMShop.src.models.order import Order
# try:
#     prod = Product('Принтер',-1000,1)
# except ValueError as e:
#     print(f'Ошибка при создании товара: {e}')
#     prod = Product('Принтер',1000,2)
# try:
#     order = Order("Petr",[])
#     order.add_product(Product('Такого товара нет',1000,1))
# except KeyError as e:
#     print(f'Ошибка при создании заказа: {e.args[0]}')
#
# try:
#     user = User('Petr','hello.com')
# except ValueError as e:
#     print(f'Ошибка при создании пользователя: {e}')
#     user = User('Petr','hello@mail.com')
#
# print()
#
# class InsufficientStockError(Exception):
#     pass

# class Product:
#     def sell(self, amount):
#         if self.quantity < amount:
#             raise InsufficientStockError(
#                 f"Товара недостаточно. На складе: {self.quantity}, требуется: {amount}"
#                 )
#         self.quantity = self.quantity - amount

# try:
#     product.sell(100)
# except InsufficientStockError as e:
#     print("Ошибка склада:", e)
#     # Логика обработки ошибки
# except Exception as e:
#     print("Другая ошибка:", e)


# ==================
# УРОК 19: СОЗДАНИЕ СОБСТВЕННЫХ ИСКЛЮЧЕНИЙ
# ==================

# Решение задачи от тимлида и Задание 1 - в файлах src/models/exceptions.py и src/models/product.py
# (проверка в REPL, в журнал не пишем)

# ВОТ РЕШЕНИЕ
# Проверка в REPL из корня SFMShop/ (в src/main.py это не пишем)
#from SFMShop.src.models.product import Product
#from SFMShop.src.models.exceptions import InsufficientStockError, SFMShopException

#product = Product("Ноутбук", 50000, 10)
#try:
    #product.sell(100)
#except InsufficientStockError as e:
   # print("Ошибка склада:", e)
#except SFMShopException as e:
   # print("Ошибка проекта:", e)

# Практика 1 Создание исключения NegativePriceError проверяем из repl поэтому тут комментим
# from SFMShop.src.models.product import Product
# from SFMShop.src.models.exceptions import NegativePriceError
#
# try:
#     product = Product("Ноутбук", -50000, 10)
# except NegativePriceError as e:
#     print("Ошибка:", e)

#Практика 2 Иерархия исключений склада
class SFMShopException(Exception):
    pass

class InsufficientStockError(SFMShopException):
    pass

class InvalidQuantityError(SFMShopException):
    pass

class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self,amount):
        if amount <= 0:
            raise InvalidQuantityError(f'Количество должно быть больше нуля, получено: {amount}')
        if self.quantity < amount:
            raise InsufficientStockError(f'Товара недостаточно. На складе: {self.quantity}, требуется: {amount}')
        self.quantity -= amount
        return self.quantity

def process_order(product,amount):
    try:
        res = product.sell(amount)
        print(f'Продано {amount} шт. товара {product.name}. Остаток: {res}')
    except InsufficientStockError as e:
        print(f'Ошибка склада: {e}')
    except SFMShopException as e:
        print(f'Ошибка проекта: {e}')

product = Product("Ноутбук", 50000, 10)
process_order(product, 3)
process_order(product, 100)
process_order(product, -5)
process_order(product, 7)

print()

#Практика 3 Иерархия исключений
#main.py
from SFMShop.src.models.product import Product
from SFMShop.src.models.order import Order
from SFMShop.src.models.exceptions import ValidationError, BusinessLogicError, SFMShopException
try:
    product = Product('Монитор',-1000,100)
except ValidationError as e:
    print(f'Ошибка валидации: {e}')

try:
    product = Product('Ноутбук',20000,10)
    product.sell(100)
except BusinessLogicError as e:
    print(f'Ошибка бизнес-логики: {e}')

try:
    order = Order('Alex',[])
except BusinessLogicError as e:
    print(f'Ошибка бизнес-логики: {e}')

