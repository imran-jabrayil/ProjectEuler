from time import time

f = open("D:\\Programming\\ProjectEuler\\Euler 21-30\\names.txt", "r")

names = sorted([i[1:-1] for i in f.read().split(",")])

f.close()

def code(name):
    num = 0
    for i in name:
        num += ord(i) - 64
    return num * (names.index(name) + 1)


summa = 0

for i in names:
    summa += code(i)

start = time()
print(summa)
print("Time {} s.".format(time() - start))