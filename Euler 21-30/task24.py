from itertools import permutations
from time import time


start = time()
print(''.join(list(permutations('0123456789', 10))[999999]))
print("Time {} s.".format(time() - start))