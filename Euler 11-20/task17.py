from time import time

dct = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8
}

def letters(x):
    if 0 < x < 20 or x in [20, 30, 40, 50, 60, 70, 80, 90]:
        return dct[x]
    elif 20 < x < 100:
        return letters(x // 10 * 10) + letters(x % 10)
    elif 100 < x < 1000:
        if x % 100 == 0:
            return letters(x // 100) + dct[100]
        return letters(x // 100) + dct[100] + 3 + letters(x % 100) 
    elif x == 100:
        return 10
    elif x == 1000:
        return 11
    else:
        return 0


def calculate(limit):
    L = []
    for i in range(1, limit):
        L.append(letters(i))
    return sum(L)


start = time()
print(calculate(1001))
print("Time {} s.".format(time() - start))