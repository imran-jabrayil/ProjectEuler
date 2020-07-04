from time import time


def calculate():
    num = 0
    d = ''
    result = 1

    while len(d) < 1000000:
        num += 1
        d += str(num)

    for i in range(0, 7):
        result *= int(d[10**i - 1])

    return result


start = time()
print(calculate())
print("Time {} s.".format(time() - start))