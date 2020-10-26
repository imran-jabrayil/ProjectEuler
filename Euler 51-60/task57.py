from time import time


def is_more(num, denom):
    return len(str(num)) > len(str(denom))


def calculate():
    num = 3
    denom = 2
    count = 0
    for i in range(999):
        num, denom = num + 2 * denom, num + denom
        if is_more(num, denom):
            count += 1
    return count 


start = time()
print(calculate())
print(f"Time: {time() - start}")