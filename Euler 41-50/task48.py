from math import pow
from time import time

start = time()
print(str(sum([i**i for i in range(1, 1001)]))[-10:])
print("Time {} s.".format(time() - start))