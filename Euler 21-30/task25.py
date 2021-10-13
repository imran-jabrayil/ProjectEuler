from time import time

def calculate():
    fib1, fib2 = 1, 1
    count = 1

    while len(str(fib1)) < 1000:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
    
    return count


start = time()
print(calculate())
print("Time {} s.".format(time() - start))