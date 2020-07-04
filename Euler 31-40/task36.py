from time import time


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def calculate():
    summa = 0

    for i in range(1, 1000000):
        if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
            summa += i
    
    return summa


start = time()
print(calculate())
print("Time {} s.".format(time() - start))