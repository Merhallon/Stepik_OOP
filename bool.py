"""
Метод __bool__
"""


class Quadrilateral:

    def __init__(self, width, height=None):
        if height is None:
            self.height = width
            self.width = width
        else:
            self.height = height
            self.width = width

    def __str__(self):
        if self.height == self.width:
            return f'Куб размером {self.width}х{self.height}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        if self.height == self.width:
            return True
        else:
            return False


class City:
    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return f"{self.name}"

    def __bool__(self):
        if self.name[-1] in ["a", "e", "i", "o", "u"]:
            return False
        else:
            return True


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"

p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"
