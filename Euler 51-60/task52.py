from time import time


def are_same(num1, num2):
    return sorted(list(str(num1))) == sorted(list(str(num2)))


def calculate():
    num = 1
    while True:
        for i in range(2, 7):
            if not are_same(num, num * i):
                break
        else:
            return num
        num += 1


start = time()
print(calculate())
print(f"Time: {time() - start}")