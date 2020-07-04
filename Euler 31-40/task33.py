from time import time

def same_frac(numer1, denom1):
    for i in str(numer1):
        if i in str(denom1) and i != '0':
            numer2 = new_num(numer1, i)
            denom2 = new_num(denom1, i)
            if numer1 * denom2 == numer2 * denom1:
                return True
    return False


def new_num(num, char):
    L = list(str(num))
    L.remove(char)
    return int(L[0])


def lowest_denom(numer, denom):
    for i in range(2, numer + 1):
        if numer % i == 0 and denom % i == 0:
            return lowest_denom(numer // i, denom // i)
    return denom


start = time()

numer, denom = 1, 1


for i in range(10, 100):
    for j in range(10, i):
        if same_frac(j, i):
            numer *= j
            denom *= i

print(lowest_denom(numer, denom))

print("Time {} s.".format(time() - start))