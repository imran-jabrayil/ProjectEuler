from math import sqrt
from time import time


def is_prime(num, lst):
    for i in lst:
        if i > sqrt(num):
            break
        if num % i == 0:
            return False
    return True


def fill_primes(num, lst):
    for i in range(lst[-1] + 1, num):
        if is_prime(i, lst):
            lst.append(i)
    return lst


def find_sum(limit):
    primes = fill_primes(limit, [2, 3])
    return sum(primes)


start = time()
print(find_sum(2000000))
print("Time {} s.".format(time() - start))