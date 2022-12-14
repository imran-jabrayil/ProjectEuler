# n^2 - n - 2x^x + 2x
# Used website - https://www.alpertron.com.ar/QUAD.HTM

n = 21
x = 15

while n <= 1e12:
    next_n = 3 * n + 4 * x - 3
    next_x = 2 * n + 3 * x - 2

    n, x = next_n, next_x

print(x)
