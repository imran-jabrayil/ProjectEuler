a, b = 1, 1
x = 2
count = 3

while len(str(x)) < 1000:
    b = a
    a = x
    x = a + b
    count += 1

print(count)