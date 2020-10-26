from time import time


def is_palindrome(num):
    return num == reverse(num)


def is_Lychrel(acc, step):
    if is_palindrome(acc):
        return False
    if step == 50:
        return True
    return is_Lychrel(acc + reverse(acc), step + 1)


def reverse(num):
    return int(str(num)[::-1])


def calculate():
    count = 0
    for num in range(1, 10000):
        if is_Lychrel(num + reverse(num), 1):
            count += 1
    return count


start = time()
print(calculate())
print(f"Time: {time() - start}")