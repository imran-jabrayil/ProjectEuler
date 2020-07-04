from time import time

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


start = time()
print(int(fact(40) / (fact(20) * fact(20))))
print("Time {} s.".format(time() - start))