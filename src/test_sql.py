from SFMShop.src.database.connection import *
from SFMShop.src.database.queries import *

def main():
    conn = connect_to_db()
    if not conn:
        return
    try:
        create_user(conn, 'Alena', 'alena@test.com')
        print('Все товары:')
        print(get_all_products(conn))

        print('Статистика:')
        print(get_order_statistics(conn))

        print('Топ товаров:')
        print(get_top_products(conn))

        print('Нахождение пользователя по id:')
        print(get_user_by_id(conn,2))

        print('История заказов:')
        print(get_user_order_history(conn,1))
    finally:
        conn.close()

if __name__ == '__main__':
    main()