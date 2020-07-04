from time import time


def primes_list(n):
    lst=[2]
    for i in range(3, n+1, 2):
    	if (i > 10) and (i%10==5):
    		continue
    	for j in lst:
    		if j*j-1 > i:
    			lst.append(i)
    			break
    		if (i % j == 0):
    			break
    	else:
    		lst.append(i)
    return lst


def is_prime(primes, num):
    if num == 1:
        return False
    for i in primes:
        if num % i == 0 and num != i:
            return False
        elif i > num:
            return True
    return True


def rotate_number(orig, num):
    num = int(str(num)[-1] + str(num)[:-1])
    if num == orig:
        return 0
    return num


start = time()

numbers = 1000000
primes = primes_list(numbers)
count = 4 #2, 3, 5, 7


for i in range(10, 1000000):
    print("{}%".format(round((i - 10) / (1000000 - 10) * 100, 3)))
    if '0' in str(i) or '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i) or '5' in str(i):
        continue
    x = is_prime(primes, i)
    temp = i
    while (x):
        temp = rotate_number(i, temp)
        if not temp:
            count += 1
            break
        x = is_prime(primes, temp)

print(count)

print("Time {} s.".format(time() - start))