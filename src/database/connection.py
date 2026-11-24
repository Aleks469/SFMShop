from psycopg2 import *
import os
from dotenv import load_dotenv
load_dotenv()

def connect_to_db():
    try:

        return connect(
            host = 'localhost',
            database = 'sfmshop',
            user = 'postgres',
            password = os.environ.get('DB_PASSWORD','password')
        )
    except Error as e:
        print(f'Произошла проблема при подключении к postgres: {e}')

def add_product(conn, name, price, quantity):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name,price,quantity) VALUES (%s, %s, %s)',
                   (name,price,quantity))
    print(f'Товар добавлен: {name}, {price}, {quantity}')
    conn.commit()
    cursor.close()

def get_all_products(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    product = cursor.fetchall()
    cursor.close()
    return product

def  update_product_price(conn, product_id, new_price):
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = %s WHERE id = %s',
                   (new_price,product_id))
    print(f'Цена обновлена: {new_price}')
    conn.commit()
    cursor.close()

def create_user(conn, name, email):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name,email) VALUES (%s, %s)',
                       (name,email))
        conn.commit()
        cursor.close()
        print(f'Пользователь создан: {name,email}')
    except Error as e:
        conn.rollback()
        print(f'Ошибка при создании пользователя: {e}')

def get_user_by_id(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id=%s',
                       (user_id,))
        user = cursor.fetchone()
        print(user)
        cursor.close()
        if user:
            id, name, email  = user[:3]
            return {'id': id, 'name': name, 'email': email}
        return None
    except Error as e:
        conn.rollback()
        print(f'Ошибка при получении пользователя {e}')


def create_order(conn, user_id, total):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (user_id,total) VALUES (%s, %s)',
                   (user_id,total))
        conn.commit()
        cursor.close()
        print(f'Заказ создан: {user_id}, {total}')
    except Error as e:
        conn.rollback()
        print(f'Ошибка при создании заказа: {e}')


def get_user_orders(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE user_id = %s',
                   (user_id,))
        res = cursor.fetchall()
        cursor.close()
        return res
    except Error as e:
        conn.rollback()
        print(f'Ошибка при получении пользоваля по id {e}')

def delete_order(conn, order_id):
    try:

        cursor = conn.cursor()
        cursor.execute('DELETE FROM orders WHERE orders.id = %s',
                   (order_id,))
        deleted = cursor.rowcount
        conn.commit()
        cursor.close()
        return deleted
    except Error as e:
        conn.rollback()
        print(f'Ошибка при удалении пользователя {e}')


