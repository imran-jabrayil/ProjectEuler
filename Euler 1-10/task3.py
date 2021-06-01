from time import time

start = time()

def max_prime_div(number):
    for i in range(2, number // 2):
        if number == i:
            break
        while not number % i:
            number /= i

    return number
        

n = 600851475143 
print(max_prime_div(n))

print("Time {} s.".format(time() - start))