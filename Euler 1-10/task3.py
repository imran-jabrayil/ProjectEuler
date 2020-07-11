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


def is_prime(num):
    return pow(2, num - 1, num) == 1


def max_prime_div(num):
    d = divs(n)
    for i in d[::-1]:
        if is_prime(i):
            return i


start = time()
n = 600851475143 
print(max_prime_div(n))
print("Time {} s.".format(time() - start))