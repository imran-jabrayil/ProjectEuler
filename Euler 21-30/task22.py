f = open("names.txt", "r")

names = sorted([i[1:-1] for i in f.read().split(",")])

def code(name):
    num = 0
    for i in name:
        num += ord(i) - 64
    return num * (names.index(name) + 1)


summa = 0

for i in names:
    summa += code(i)

print(summa)