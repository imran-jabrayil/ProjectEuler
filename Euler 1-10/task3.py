from time import time
from math import sqrt


def divs(n):
    x = 2
    divisors = set()
    while n != 1:
        if n % x == 0:
            n //= x
            divisors.add(x)
        else:
            x += 1
            if x > sqrt(n):
                divisors.add(n)
                break
    return sorted(list(divisors))


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


def max_prime_div(num):
    d = divs(n)
    primes = fill_primes(d[-1], [2, 3])
    for i in d[::-1]:
        if is_prime(i, primes):
            return i


start = time()
n = 600851475143 
print(max_prime_div(n))
print("Time {} s.".format(time() - start))