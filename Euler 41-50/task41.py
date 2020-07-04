from itertools import permutations
from time import time


def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


def calculate():
    numbers = []
    for i in range(9, 0, -1):
        numbers.extend(list(map(int, [''.join(c) for c in permutations("".join([str(x) for x in range(1, i + 1)]))])))
    numbers.sort()

    for i in numbers[::-1]:
        if is_prime(i):
            return i


start = time()
print(calculate())
print("Time {} s.".format(time() - start))