"""Для выражения относительной силы шахматистов
используется система рейтингов.
Наиболее популярная система рейтингов, которая используется
Международной шахматной федерацией (ФИДЕ),
большинством других шахматных федераций и игровых шахматных сайтов,
является система рейтингов Эло.

В зависимости от выступлений на различных соревнованиях
каждому шахматисту начисляются баллы в его рейтинг.
Давайте с вами реализуем класс ChessPlayer и научимся сравнивать рейтинги шахматистов между собой.
"""


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer):
            return other.rating == self.rating
        elif isinstance(other, int):
            return other == self.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, ChessPlayer):
            return other.rating < self.rating
        elif isinstance(other, int):
            return other < self.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, ChessPlayer):
            return other.rating > self.rating
        elif isinstance(other, int):
            return other > self.rating
        else:
            return 'Невозможно выполнить сравнение'

magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"