
# 1 часть Создайте класс Registration, который пока будет проверять только введенный логин.
# Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.
#
# В классе Registration необходимо реализовать:
#
# метод __init__ принимающий один аргумент логин пользователя.
# Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3).
# То есть когда отработает данный код

# def __init__(self, логин):
#     self.login = логин # передаем в сеттер login значение логин
# должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения
#
# Cвойство геттер login, которое возвращает значение self.__login;
# Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
# логин, так как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@», вызываем исключение при помощи строки raise ValueError("Логин должен содержать один символ '@'")
# логин должен содержать символ точки «.» после символа «@».В случае, если после @ нету точки, вызываем исключение при помощи строки raise ValueError("Логин должен содержать символ '.'")
# Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login
# Про исключения и команду raise мы с вами поговорим позже, просто вставляйте эту строчку как есть
# if error:
#     raise ValueError("Login must include at least one ' @ '")
from audioop import error
# часть 2
# У нас уже имеется с предыдущего урока класс Registration. Давайте добавим в него следующее:
#
# в метод  __init__ добавляется еще один аргумент: пароль. Как в примере с логином, вы должны будете сохранить переданный пароль через password через сеттер  password (см пункт 3 в этом задании). Примерный код метода __init__
# def __init__(self, логин, пароль):
#     self.login = логин # передаем в сеттер login значение логин
#     self.password = пароль # передаем в сеттер password значение пароль
# Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из пункта 3 для проверки валидности переданных значений
#
# Свойство геттер password, которое возвращает значение self.__password;

# Свойство сеттер password, принимает значение нового пароля.
# Его необходимо перед сохранением проверить на следующее:
# новое значение пароля должно быть строкой(не список, словарь и т.д. )
# в противном случае вызываем исключение TypeError("Пароль должен быть строкой")

# Длина нового пароля должна быть от 5 до 11 символов,
# в противном случае вызывать исключение ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

# Новый пароль должен содержать хотя бы одну цифру.
# Для этого создаем staticmethod is_include_digit , который проходит по всем элементам строки и проверяет наличие цифр.
# В случае отсутствия цифрового символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')

# Строка password должна содержать элементы верхнего и нижнего регистра.
# Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элемента строчки на регистр.
# В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

# Строка password помимо цифр должна содержать только латинские символы.
# Для этого создайте staticmethod is_include_only_latin ,
# который проверяет каждый элемент нового значения на принадлежность к латинскому алфавиту(проверка должна быть как в верхнем, так и нижнем регистре).
# В случае, если встретится нелатинский символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит').

# Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
#  С помощью staticmethod создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле.
#  Если значение совпадет со значением из файла, то в сеттер вызываем исключение: ValueError('Ваш пароль содержится в списке самых легких')
from string import ascii_letters, octdigits


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_login: str):
        if '@' not in new_login:
            raise ValueError("Логин должен содержать один символ '@'")
        if new_login.count('.') != 1:
            raise ValueError("Логин должен содержать символ '.'")
        if new_login.index('@') > new_login.index('.'):
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = new_login

    @password.setter
    def password(self, new_password):
        if not isinstance(new_password, str):
            raise TypeError("Пароль должен быть строкой")
        if not(5 <= len(new_password) <= 11):
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        self.is_include_digit(new_password)
        self.is_include_all_register(new_password)
        self.is_include_only_latin(new_password)
        self.check_password_dictionary(new_password)
        self.__password = new_password

    @staticmethod
    def is_include_digit(new_password):
        error_int = 0
        for el in new_password:
            if el in octdigits:
                error_int += 1
        if error_int == 0:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(new_password):
        if not(new_password.lower() != new_password and new_password.upper() != new_password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

    @staticmethod
    def is_include_only_latin(new_password):
        for el in new_password:
            if el in octdigits:
                continue
            if el not in ascii_letters:
                raise ValueError('Пароль должен содержать только латинский алфавит')

    @staticmethod
    def check_password_dictionary(new_password):
        f = open('easy_passwords.txt', 'r')
        for password in f:
            if password.replace('\n', '') == new_password:
                raise ValueError('Ваш пароль содержится в списке самых легких')

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
# print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
# r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 43  # raise TypeError("Пароль должен быть строкой")
# r1.password = 'KissasSAd1f'  # ValueError: Ваш пароль содержится в списке самых легких