# Файл order_processor.py

# 1. Работа со строками и файлами
def load_orders_from_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            res = file.readlines()
            orders = []
            for el in res:
                orders.append(el.strip())
            return orders
    except FileNotFoundError:
        print('Файл не найден')


# 2. Работа с числами и условными операторами
def calculate_order_total(price, discount_rate):
    if isinstance(price,int):
        total = round(price * (1 - discount_rate),2)
        return total

def get_discount_by_total(total):
    if total <= 0:
        return 0
    elif total > 10000:
        discount = 0.15
    elif total > 5000:
        discount = 0.1
    else:
        discount = 0.05
    return discount

# 3. Работа со списками и циклами
def process_orders(orders_data):
    amount = []
    for el in orders_data:
        try:
            number, summ, status, user = el.split(':')
            count = get_discount_by_total(int(summ))
            total = calculate_order_total(int(summ),count)
            customers ={'order_id':number,'total':total,'status':status,'user': user}
            amount.append(customers)
        except ValueError:
            print('Введены некорректные данные')
    return amount

# 4. Работа со словарями и множествами

def analyze_orders(processed_orders):
    stats = {'total_orders': 0,'total_sum': 0,'by_status': {},'unique_users': set()}
    for el in processed_orders:
        stats['total_orders'] = stats.get('total_orders',0) + 1
        stats['total_sum'] = stats.get('total_sum',0) + el['total']
        by_status = el['status']
        stats['by_status'][by_status] = stats['by_status'].get(by_status,0) + 1
        stats['unique_users'].add(el['user'])
    stats['unique_users'] = list(stats['unique_users'])
    return stats

#5. Работа с функциями и модулями

def process_order_file(input_file, output_file):
    file = load_orders_from_file(input_file)
    processing = process_orders(file)
    analyze = analyze_orders(processing)
    with open(output_file,'w',encoding='utf-8') as file:
        file.write(f'Обработано заказов: {analyze["total_orders"]}\n')
        file.write(f'Общая сумма: {analyze["total_sum"]}\n')
        file.write('По статусам: ' + ", ".join(f'{k} : {v}' for k,v in analyze["by_status"].items()) + '\n')
        file.write(f'Уникальных пользователей: {len(analyze["unique_users"])}')


