from math import sqrt
from time import time


def word_value(word):
    value = 0
    for i in word:
        value += ord(i) - 64
    return value

def is_triangle(word):
    value = word_value(word)
    temp = discriminant(value * 2)
    if temp == int(temp):
        return True
    return False

def discriminant(num):
    d = 1 + 4 * num
    return (-1 + sqrt(d)) / 2


#importing words
f = open("D:\\Programming\\ProjectEuler\\Euler 41-50\\words.txt", "r")
words = [i[1:-1] for i in f.read().split(",")]
f.close()


count = 0
for i in words:
    if is_triangle(i):
        count += 1


start = time()
print(count)
print("Time {} s.".format(time() - start))