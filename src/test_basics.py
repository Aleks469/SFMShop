#Файл main.py

from utils.order_processor import process_order_file

process_order_file("data/orders.txt", "data/processed_orders_report.txt")

