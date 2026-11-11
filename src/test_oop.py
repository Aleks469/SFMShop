class Car:

    def __init__(self,name,price):
        self._name = name
        self.__price = price
    def __str__(self):
        return f'У Вас машина {self._name}'
car = Car('Audi',12500)
print(car._name)
print(car._Car__price)