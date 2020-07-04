from itertools import permutations
from time import time
from math import sqrt


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


def check_number(num, lst, count):
    if is_prime(num, lst):
        return False
    index = 0
    fracts = set()
    while num != 1 and index < len(lst):
        if num % lst[index] == 0:
            num /= lst[index]
            fracts.add(lst[index])
        else:
            index += 1
    return len(fracts) == count and index < len(lst)


def find_answer(count):
    num = 1
    L = []
    primes = [2, 3]
    
    while len(L) < count:
        num += 1
        primes = fill_primes(num, primes)
        if check_number(num, primes, count):
            if len(L) == 0 or L[-1] + 1 == num:
                L.append(num)
            else:
                L = [num]
    return L[0]


start = time()
print(find_answer(4))
print("Time {} s.".format(time() - start))