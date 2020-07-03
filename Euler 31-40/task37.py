from time import sleep

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_trunc_prime_l2r(num):
    if not is_prime(num):
        return False
    if num < 10 and is_prime(num):
        return True
    return is_trunc_prime_l2r(int(str(num)[1:]))

def is_trunc_prime_r2l(num):
    if not is_prime(num):
        return False
    if num < 10 and is_prime(num):
        return True
    return is_trunc_prime_r2l(int(str(num)[:-1]))

def is_trunc_prime(num):
    return is_trunc_prime_l2r(num) and is_trunc_prime_r2l(num)



count = 0
num = 11

L = []

while count < 11:
    print("Number: {}, count: {}".format(num, count))
    if (str(num)[0] == '1' or str(num)[0] == '4' or str(num)[0] == '6' or str(num)[0] == '8' or str(num)[0] == '9') or \
        ('0' in str(num)[1:] or '2' in str(num)[1:] or '4' in str(num)[1:] or '6' in str(num)[1:] or '8' in str(num)[1:] or '5' in str(num)[1:]):
        num += 2
        continue
    if is_trunc_prime(num):
        count += 1
        L.append(num)
    num += 2

print(L)
print(sum(L))

