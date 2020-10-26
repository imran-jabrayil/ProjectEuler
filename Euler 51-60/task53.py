from time import time


def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)


def comb(n, r):
    return fact(n) / (fact(r) * fact(n - r))


def calculate():
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if comb(n, r) > 1000000:
                count += 1
    return count


start = time()
print(calculate())
print(f"Time: {time() - start}")