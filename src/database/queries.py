from psycopg2 import *
import os
from dotenv import load_dotenv
load_dotenv()

conn = connect(
        host = 'localhost',
        database = 'sfmshop',
        user = 'postgres',
        password = os.environ.get('DB_PASSWORD','password'))

def get_orders_with_products(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""SELECT orders.id,
                   products.name,
                   order_items.quantity,
                   products.price FROM orders
                   INNER JOIN order_items ON orders.id = order_items.order_id
                   INNER JOIN products ON order_items.product_id = products.id 
                   WHERE orders.user_id  = %s""", (user_id,))

    res = cursor.fetchall()
    cursor.close()
    return res

def statistics(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT user_id,
                   COUNT(*) as order_count,
                   SUM(total) as sum
                   FROM orders
                   GROUP BY user_id
                   ORDER BY sum DESC""")
    res = cursor.fetchall()
    cursor.close()
    return res

def get_user_order_history(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""SELECT orders.id,products.name,order_items.quantity,orders.created_at
                    FROM orders 
                    INNER JOIN order_items ON orders.id = order_items.order_id
                    INNER JOIN products ON order_items.product_id = products.id
                    WHERE orders.user_id = %s
                    ORDER BY orders.created_at DESC""", (user_id,))

    res = cursor.fetchall()
    cursor.close()
    return res


def get_order_statistics(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT users.id,users.name, COUNT(orders.id) as order_count, COALESCE(SUM(orders.total), 0) as sum
                    FROM users
                    LEFT JOIN orders ON users.id = orders.user_id
                    GROUP BY users.id""")

    res = cursor.fetchall()
    cursor.close()
    return res

def get_top_products(conn, limit=5):
    cursor = conn.cursor()
    cursor.execute("""SELECT products.name, SUM(order_items.quantity) as sold
                    FROM products
                    INNER JOIN order_items ON products.id = order_items.product_id
                    GROUP BY products.id
                    ORDER BY sold DESC
                    LIMIT %s""", (limit,))
    res = cursor.fetchall()
    cursor.close()
    return res

