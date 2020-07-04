from itertools import permutations
from time import time


def substring_div(num, lst):
    for i in range(1, 8):
        if int(num[i] + num[i+1] + num[i+2]) % lst[i-1] != 0:
            return False
    return True


start = time()


numbers = [''.join(i) for i in permutations("0123456789") if i[0] != '0']

summa = 0
primes = [2, 3, 5, 7, 11, 13, 17]

for i in numbers:
    if substring_div(i, primes):
        summa += int(i)


print(summa)
print("Time {} s.".format(time() - start))