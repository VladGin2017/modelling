import matplotlib.pyplot as plt
import random

print(f'Генератор Random()')
N = int(input("N: "))
K = int(input("K: "))
y = range(N)
x_1 = []
numbers_1 = [0] * K
ksi = 0


def gen_1():
    for k in y:
        rand_1 = random.uniform(0, 1)
        x_1.append(rand_1)
        inter_1 = rand_1 / (1 / K)
        numbers_1[int(inter_1)] += 1

    p_i = 1 / K
    i = 0
    ksi = 0
    while i != K:
        ksi += (((numbers_1[i] - p_i * N) ** 2) / (p_i * N))
        i += 1
    print(f'Хи квадрат: {ksi}')

    i = 0
    Ex = 0
    while i != N:
        Ex += x_1[i]
        i += 1
    Ex = (1 / N) * Ex

    i = 0
    S2x = 0
    while i != N:
        S2x += ((x_1[i] + Ex) ** 2)
        i += 1
    S2x = S2x / N

    offset = 1
    while offset <= K / 2:
        a = 0
        i = 0
        while i < N - offset:
            a += (x_1[i] - Ex) * (x_1[i + offset] - Ex)
            i += 1
        a = a / ((N - offset) * S2x)
        print(f'a(tao) %f' % a)
        print(f'tao: {offset}')
        offset += 1


def graph():
    i = 0
    bins = [0] * K
    j = 0
    while i < K:
        bins[i] = j
        j += 1 / K
        i += 1


    # plt.figure(figsize=(50, 5))
    plt.hist(x_1, bins=[i for i in bins], color='green')
    plt.title('ГСЧ стандартной библиотеки random()')
    plt.xlabel(f'Кол-во интервалов (Всего {K})')
    plt.ylabel(f'Кол-во чисел (Всего {N})')
    plt.savefig('gen_1.png')
    # plt.show()

gen_1()
graph()