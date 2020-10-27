from time import time


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def calculate():
    prime_count = level = 0
    count = 1
    while True:
        level += 1
        square = (level * 2 + 1) ** 2
        for i in range(4):
            num = square - level * 2 * i
            count += 1
            if is_prime(num):
                prime_count += 1
        if prime_count / count < 0.1:
            break
    return level * 2 + 1


start = time()
print(calculate())
print(f"Time: {time() - start}")