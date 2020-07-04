from time import time

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

start = time()
print(sum(list(map(int, list(str(fact(100)))))))
print("Time {} s.".format(time() - start))