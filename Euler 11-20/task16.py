from time import time

def calculate(num):
    sum(list(map(int, list(str(num)))))

start = time()
print(calculate(2**1000))
print("Time {} s.".format(time() - start))