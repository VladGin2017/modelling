import matplotlib.pyplot as plt
from numpy.random import rand

print(f'Генератор модуля NumPy')
N = int(input("N: "))
K = int(input("K: "))
y = range(N)
x_2 = []
numbers_2 = [0] * K
ksi = 0
offset = 1


def gen_2():
    for k in y:
        rand_2 = rand()
        x_2.append(rand_2)
        inter_2 = rand_2 / (1 / K)
        numbers_2[int(inter_2)] += 1


    p_i = 1 / K
    i = 0
    ksi = 0
    while i != K:
        ksi += (((numbers_2[i] - p_i * N) ** 2) / (p_i * N))
        i += 1
    print(f'Хи квадрат: {ksi}')

    i = 0
    Ex = 0
    while i != N:
        Ex += x_2[i]
        i += 1
    Ex = (1 / N) * Ex

    i = 0
    S2x = 0
    while i != N:
        S2x += ((x_2[i]) ** 2) - (Ex ** 2)
        i += 1
    S2x = S2x / N

    offset = 1
    while offset <= K / 2:
        a = 0
        i = 0
        while i < N - offset:
            a += (x_2[i] - Ex) * (x_2[i + offset] - Ex)
            i += 1
        a = a / (N - offset) * S2x
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
    plt.hist(x_2, bins=[i for i in bins], color='green')
    plt.title('ГСЧ библиотеки Numpy')
    plt.xlabel(f'Кол-во интервалов (Всего {K})')
    plt.ylabel(f'Кол-во чисел (Всего {N})')
    plt.savefig('gen_2.png')
    #plt.show()


gen_2()
graph()