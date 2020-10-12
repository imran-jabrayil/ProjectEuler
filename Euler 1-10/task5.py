from time import time


def is_prime(num, lst):
    for i in lst:
        if num % i == 0:
            return False
    return True


def fill_primes(limit, lst):
    for i in range(lst[-1] + 1, limit + 1):
        if is_prime(i, lst):
            lst.append(i)
    return lst


def prime_divs(num, lst):
    L = []
    for i in lst:
        while num % i == 0:
            num /= i
            L.append(i)
    return L


def calc(limit):
    primes = fill_primes(limit, [2, 3])
    result = 1
    for i in range(2, limit + 1):
        temp = prime_divs(result, primes)
        for j in prime_divs(i, primes):
            if j not in temp:
                result *= j
            else:
                temp.remove(j)
    return result


start = time()
print(calc(20))
print(time() - start)