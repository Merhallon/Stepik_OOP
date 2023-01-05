from concurrent import futures
import math
import sys
"""
Каждый работник возвращает значение по мере вычисления
"""


def calc(val):
    result = math.sqrt(float(val))  # вычисляем квадратный корень
    return val, result


def use_threads(num, values):
    """
    Задействуем пул потоков
    """
    with futures.ThreadPoolExecutor(num) as tex:
        tasks = [tex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()  # есть yield поэтому это функция генератор
            # благодаря этому возвращаем значение на каждой итерации


def use_processes(num, values):
    """
    Задействуем пул процессов
    """
    with futures.ProcessPoolExecutor(num) as pex:
        tasks = [pex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()


def main(workers, values):
    print(f'Using {workers} workers for {len(values)} values')
    print(f'Using threads:')
    for val, result in use_threads(workers, values):
        print(f'{val} {result:.4f}')
    print(f'Using processes:')
    for val, result in use_processes(workers, values):
        print(f'{val} {result:.4f}')


if __name__ == "__main__":
    workers = 3
    if len(sys.argv) > 1:
        workers = int(sys.argv[1])
    values = list(range(1, 6))  # 1...5
    main(workers, values)
