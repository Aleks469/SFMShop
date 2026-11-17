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
        print(f'Заказ создан: user_id={user_id}, total={total}')
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
        print(f'Ошибка при получении пользователя по id {e}')


def main():
    conn = connect_to_db()
    try:
        create_user(conn, 'Иван', 'ivan@test.ru')
        print(f'Пользователь найден:{get_user_by_id(conn,1)}')
        create_order(conn, 1, 50000)
        print(f'Заказы пользователя {get_user_orders(conn,1)}')
    finally:
        conn.close()


if __name__ == '__main__':
    main()

