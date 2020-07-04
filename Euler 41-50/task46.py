from math import sqrt
from time import time


def is_prime(num, lst):
    for i in lst:
        if num % i == 0:
            return False
    return True


def fill_primes(num, lst):
    for i in range(lst[-1] + 1, num):
        if is_prime(i, lst):
            lst.append(i)
    return lst


def is_sum(num, lst):
    for i in lst:
        temp = sqrt( (num - i) / 2 )
        if temp == int(temp):
            return True
    return False


def find_answer():
    primes = [2, 3]
    odd = 1
    while True:
        odd += 2
        primes = fill_primes(odd, primes)
        if is_prime(odd, primes):
            continue
        if not is_sum(odd, primes):
            return odd


start = time()
print(find_answer())
print("Time {} s.".format(time() - start))