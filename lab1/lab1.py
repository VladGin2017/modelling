import random
import typing as tp

N = 1000000
K = 100
a_ = 0.25


def f(x: float) -> float:
    if x > 0 and x <= 2:
        return a_ * ((x + 3) / 2)
    else:
        return 0


def method_rejections() -> float:
    array = []
    a = 0
    b = 2
    c = 1
    while True:
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        tmp = f(a + (b - a) * x1)
        if tmp > c * x2:
            return a + (b - a) * x1


def distribution_density() -> tp.List[int]:
    hit = [0] * K
    x = []
    y_1 = []
    m = 2 / K
    f = open('density.txt', 'w')
    for i in range(N):
        rand = method_rejections()
        x.append(rand)
        y = a_ * (x[i] + 5)
        y_1.append(y)
        inter = rand / m
        hit[int(inter)] += 1
        f.write(str(x[i]) + '\t' + str(y) + '\n')
    f.close()
    return hit


def repeat() -> tp.List[int]:
    residue_chance = 1.0
    chance_hit = [0] * K
    hit = [0] * K

    for i in range(K - 1):
        chance_hit[i] = random.uniform(0, 1) % residue_chance
        residue_chance -= chance_hit[i]
    chance_hit[-1] = residue_chance

    for i in range(N):
        chance = random.uniform(0, 1)
        sum = 0.0
        for j in range(K):
            sum += chance_hit[j]
            if (chance < sum):
                hit[j] += 1
                break

    for i in range(K):
        chance_hit[i] = chance_hit[i] * 100000
    f = open('repeat.txt', 'w')
    i = 0
    while i != K:
        f.write(str(hit[i]) + '\t' + str(chance_hit[i]) + '\n')
        i += 1
    f.close()
    return hit, chance_hit


def no_repeat() -> tp.List[int]:
    k = 3 / 4 * K
    hit = [0] * K
    part = N / k + 1

    for i in range(int(part)):
        nums = [nums for nums in range(K)]
        if i == part - 1:
            k = N % k
        for j in range(int(k)):
            p = 1.0 / (K - j)
            it = int(random.uniform(0, 1) * 1.0 / p)
            hit[nums[it]] += 1
            nums.pop(it)
    f = open('norepeat.txt', 'w')
    i = 0
    while i != K:
        f.write(str(hit[i]) + '\t' + str(N / K) + '\n')
        i += 1
    f.close()
    return hit


distribution_density()
repeat()
no_repeat()