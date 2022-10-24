# магические метода __add__ __mul__ __str__

class Vector:
    def __init__(self, *args):
        a = []
        for x in args:
            if isinstance(x, int):
                a.append(x)
        self.values = sorted(a)

    def __str__(self):
        if not self.values:
            return "Пустой вектор"
        else:
            s = ', '.join(map(str, sorted(self.values)))
            return f'Вектор({s})'

    def __add__(self, other):
        if isinstance(other, int):
            new_values = [x + other for x in self.values]
            return Vector(*new_values)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                # new_values = [self.values[x] + other.values[x] for x in range(len(self.values))]
                new_values = [sum(x) for x in zip(self.values, other.values)]
                return Vector(*new_values)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            new_values = [x * other for x in self.values]
            return Vector(*new_values)
        elif isinstance(other, Vector):
            if len(other.values) == len(self.values):
                # new_values = [self.values[x] * other.values[x] for x in range(len(self.values))]
                new_values = [x[0]*x[1] for x in zip(self.values, other.values)]
                return Vector(*new_values)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1,2,3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2)  # печатает "Вектор(3, 4, 5)"

v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"

v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"

v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"

v5 + 'hi' # печатает "Вектор нельзя сложить с hi"