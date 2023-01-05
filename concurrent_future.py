from concurrent import futures
import math
import time
import sys


def calc(val):
    time.sleep(1)
    result = math.sqrt(float(val))  # вычисляем квадратный корень
    return result


def use_treads(num, values):
    """
    Задействуем пул потоков
    """
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        results = tex.map(calc, values)
    t2 = time.time()
    return t1 - t2


def use_processes(num, values):
    """
    Задействуем пул процессов
    """
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as pex:
        results = pex.map(calc, values)
    t2 = time.time()
    return t1 - t2


def main(workers, values):
    print(f'Using {workers} workers for {len(values)} values')
    t_sec = use_treads(workers, values)
    print(f'Treads took {t_sec:.4f} second')
    p_sec = use_processes(workers, values)
    print(f'Processes took {p_sec:.4f} second')


if __name__ == "__main__":
    workers = int(sys.argv[1])
    values = list(range(1, 6))  # 1...5
    main(workers, values)
