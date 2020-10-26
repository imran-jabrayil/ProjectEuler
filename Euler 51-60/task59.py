from string import ascii_lowercase


def read_nums(fn):
    with open(fn, 'r') as f:
        nums = list(int(i) for i in f.read().split(','))
    return nums


def xor(num1, num2):
    return num1 ^ num2


def variants():
    for i in ascii_lowercase:
        for j in ascii_lowercase:
            for k in ascii_lowercase:
                yield i + j + k


def calculate():
    nums = read_nums('p059_cipher.txt')
    
    f = open('cart.txt', 'w+')
    for i in variants():
        result = ''
        code = [ord(x) for x in i]
        for j in range(len(nums)):
            result += chr(xor(nums[j], code[j % 3]))
        f.write(result + '\n\n')
        if result.casefold().count('the ') > 2:
            return sum([ord(i) for i in result])
    return None
    


print(calculate())
