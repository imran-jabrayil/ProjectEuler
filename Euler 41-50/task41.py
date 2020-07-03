def primes_list(n):
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                print("Prime:", i)
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            print("Prime:", i)
            lst.append(i)
    return lst

def is_prime(num, lst):
    if num in lst:
        return True
    return False

def pandigital(num):
    if len(set(str(num))) == num and '0' not in str(num):
        return True
    return False

print("Primes are not ready")
primes = primes_list(987654321)
print("Primes are ready")

for i in range(987654321, 2, -1):
    print(i)
    if pandigital(i) and is_prime(i, primes):
        print("The answer is:", i)
        break
