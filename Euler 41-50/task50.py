from math import sqrt
from time import time
from itertools import permutations


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


def longest_sum(limit):
    primes = fill_primes(limit, [2, 3])
    count = len(primes)

    summa, limit = 0, 0
    while summa < primes[-1]:
        summa += primes[limit]
        limit += 1

    for i in range(limit, 0, -1):
        for j in range(count - i + 1):
            temp = sum(primes[j:j + i])
            if temp in primes:
                return temp 
            if temp > primes[-1]:
                break


start = time()
print(longest_sum(1000000))
print("Time {} s.".format(time() - start))