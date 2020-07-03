num = 0
d = ''

while len(d) < 1000000:
    num += 1
    d += str(num)

result = 1

for i in range(0, 7):
    result *= int(d[10**i - 1])

print(result)