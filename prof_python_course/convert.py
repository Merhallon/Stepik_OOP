
def convert(input_string: str):
    """Реализуйте функцию convert(), которая принимает один аргумент:
    string — произвольная строка
    Функция должна возвращать строку string:
    полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
    полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
    полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
    """
    upper, lowe = 0, 0
    input_string.replace(' ', '')
    for sing in input_string:
        if sing.isupper():
            upper += 1
        elif sing.islower():
            lowe += 1
    if lowe < upper:
        return input_string.upper()
    else:
        return input_string.lower()

