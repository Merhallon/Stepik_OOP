# Product. Это класс, описывающий товар. В нем должно быть реализовано:
#
# метод __init__, принимающий на вход имя товара и его стоимость.
# Эти значения необходимо сохранить в атрибутах name и price
# Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:
#
# метод __init__, принимающий на вход логин пользователя и необязательный аргумент баланс его счета(по умолчанию 0).
# Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
# метод __str__, возвращающий строку вида «Пользователь {login}, баланс - {balance}»
# Cвойство геттер balance, которое возвращает значение self.__balance;
# Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
# метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
# метод payment  принимает числовое значение, которое должно списаться с баланса пользователя.
# Если на счете у пользователя не хватает средств, то необходимо вывести фразу  «Не хватает средств на балансе.
# Пополните счет» и вернуть False.
# Если средств хватает, списываем с баланса у пользователя указанную сумму и возвращаем True
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance: int):
        self.__balance = new_balance

    def deposit(self, i: int):
        self.__balance += i

    def payment(self, i: int):
        if self.__balance - i < 0:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance = self.__balance - i
            return True

billy = User('billy@rambler.ru')
print(billy) # Пользователь billy@rambler.ru, баланс - 0
billy.deposit(100)
billy.deposit(300)
print(billy) # Пользователь billy@rambler.ru, баланс - 400
billy.payment(500) # Не хватает средств на балансе. Пополните счет
billy.payment(150)
print(billy) # Пользователь billy@rambler.ru, баланс - 250