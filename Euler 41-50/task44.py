from math import sqrt

def is_pentagonal(num):
    d = 1 + 24 * num
    n = (1 + sqrt(d)) / 6
    return int(n) == n


def pentag_number(index):
    return int((index + 1) * (3 * (index + 1) - 1) / 2)


L = [1]

k = 0

while k > -1:
    if len(L) <= k:
        L.append(pentag_number(k))
    for j in range(0, k):
        if is_pentagonal(L[k] + L[j]) and is_pentagonal(L[k] - L[j]):
            print(L[k] - L[j])
            k = -2
            break
    k += 1
