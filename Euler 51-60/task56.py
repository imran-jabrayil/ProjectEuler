from time import time


def calculate():
    result = 0
    for a in range(1, 100):
        for b in range(1, 100):
            temp = sum(list(map(int, str(a ** b))))
            if temp > result:
                result = temp
    return result


start = time()
print(calculate())
print(f"Time: {time() - start}")