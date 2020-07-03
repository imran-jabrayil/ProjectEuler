def is_palindrome(num):
    return str(num) == str(num)[::-1]


sum = 0

for i in range(1, 1000000):
    if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
        sum += i

print(sum)
