from itertools import permutations
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


def numbers_list():
    primes = fill_primes(10000, [2, 3])
    nums = [i for i in primes if 1000 <= i <= 9999]
    L = []
    for i in nums[:-2:]:
        for j in nums[nums.index(i) + 1:]:
            for k in nums[nums.index(j) + 1:]:
                if i - j == j - k and set(str(i)) == set(str(j)) == set(str(k)):
                    L.append(str(i) + str(j) + str(k))
    return L[-1]


print(numbers_list())