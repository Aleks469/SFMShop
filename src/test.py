# Задача 1
student = {
    "name": "Alex",
    "age": 20,
    "grade": 4
}
print(student['name'])
student['age'] = 21
student['city'] = 'Moscow'
del student['grade']
print('age' in student)


# Задача № 2 — Подсчёт символов
a = 'hello'
res = {}
for el in a:
    res[el] = res.get(el,0) + 1
print(res)

# Задача № 3 — Словарь покупок
prices = {
    "apple": 50,
    "banana": 30,
    "orange": 70
}
def get_price(prices, product):

    return prices.get(product,'Not found')
get_price(prices, "apple")

#🟢 Задача № 4 — Объединение словарей
a = {"apple": 2, "banana": 3}
b = {"apple": 5, "orange": 4}
result = {}
for key, value in a.items():
    result[key] = result.get(key,0) + value
for key, value in b.items():
    result[key] = result.get(key,0) + value
print(result)

# Задача № 5 — Подсчёт слов

def word_count(text):
    slovar = {}
    for el in text.lower().split():
        slovar[el] = slovar.get(el,0) + 1
    return slovar


print(word_count('cat dog cat bird dog cat'))

#Задача № 6 — Инвертирование словаря
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
new_data ={}
for key, value in data.items():
    new_data[value] = key
print(data)

#Задача № 7 — Найди лидера голосования
votes = [
    "Alice", "Bob", "Alice",
    "Charlie", "Bob", "Alice",
    "Bob", "Alice"
]
vot = {}
for el in votes:
    vot[el] = vot.get(el,0) + 1
print(vot)
print(max(vot,key = lambda x: vot[x]))

# Задача № 8 — Группировка по длине
words = [
    "cat", "dog", "apple",
    "hi", "book", "sun", "car"
]
lt = {}
for el in words:
    lt[len(el)] = lt.get(len(el),[])
    lt[len(el)].append(el)
print(lt)

