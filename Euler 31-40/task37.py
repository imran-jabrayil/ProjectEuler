from time import time
from math import sqrt


def is_prime(num, lst):
    if num == 1 or num == 0:
        return False
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


def is_trunc_prime_l2r(num, lst):
    if not is_prime(num, lst):
        return False
    if num < 10 and is_prime(num, lst):
        return True
    return is_trunc_prime_l2r(int(str(num)[1:]), lst)


def is_trunc_prime_r2l(num, lst):
    if not is_prime(num, lst):
        return False
    if num < 10 and is_prime(num, lst):
        return True
    return is_trunc_prime_r2l(int(str(num)[:-1]), lst)


def is_trunc_prime(num, lst):
    return is_trunc_prime_l2r(num, lst) and is_trunc_prime_r2l(num, lst)


start = time()

count = 0
num = 11

L = []
primes = [2, 3]

while count < 11:
    primes = fill_primes(num, primes)
    if (str(num)[0] == '1' or str(num)[0] == '4' or str(num)[0] == '6' or str(num)[0] == '8' or str(num)[0] == '9') or \
        ('0' in str(num)[1:] or '2' in str(num)[1:] or '4' in str(num)[1:] or '6' in str(num)[1:] or '8' in str(num)[1:] or '5' in str(num)[1:]):
        num += 2
        continue
    if is_trunc_prime(num, primes):
        count += 1
        L.append(num)
    num += 2


print(sum(L))

print("Time {} s.".format(time() - start))